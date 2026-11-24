"""Check the assessment's packaged OutSystems solution without a live environment."""

from pathlib import Path
import unittest
import xml.etree.ElementTree as ET
from zipfile import ZipFile


PACKAGE = (
    Path(__file__).resolve().parents[1]
    / "outsystems"
    / "application-export"
    / "CarParkSolution-v1.osp"
)
EXPECTED_MODULES = {
    "CarPark",
    "CPA_Common_Lib",
    "CPA_CS",
    "CPA_Sync_CS",
    "DataGov_IS",
    "OneMap_IS",
    "OpenstreetMapPlugin",
}


class SolutionPackageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.archive = ZipFile(PACKAGE)
        cls.addClassCleanup(cls.archive.close)

    def test_archive_integrity(self):
        self.assertIsNone(self.archive.testzip(), "OSP contains a corrupt entry")

    def test_manifest_identifies_solution(self):
        manifest = ET.fromstring(self.archive.read("Manifest.xml"))
        solution = manifest.find("./Solutions/Solution")
        self.assertIsNotNone(solution)
        self.assertEqual(solution.get("Name"), "CarParkSolution")
        self.assertTrue(manifest.get("HubServerVersion", "").startswith("11."))
        version = solution.find("Version")
        self.assertIsNotNone(version)
        self.assertEqual(version.get("Name"), "V1")

    def test_expected_modules_are_included(self):
        manifest = ET.fromstring(self.archive.read("Manifest.xml"))
        declared_modules = {
            module.get("Name")
            for module in manifest.findall(
                "./Solutions/Solution/Applications/Application/Modules/Module"
            )
        }
        for name in sorted(EXPECTED_MODULES):
            with self.subTest(module=name):
                self.assertIn(name, declared_modules)
                entry = self.archive.getinfo(f"CarParkSolution/{name}.oml")
                self.assertGreater(entry.file_size, 0)
