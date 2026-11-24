# Automated checks and application testing

## Run the package checks

From the repository root, run the tests with Python 3.9 or later. They require only the Python standard library and the committed OSP.

```bash
python -m unittest discover -s tests -v
```

The three package checks passed locally against the included V1 archive. They verify that the OSP archive can be read, that its manifest identifies `CarParkSolution` V1 on OutSystems 11, and that the expected app, service, and integration module files and map plugin are packaged. The `Assessment checks` GitHub Actions workflow is configured to run the same checks on GitHub.

## Application-level tests to include before submission

Add the runnable test source or an OutSystems test module export, the environment prerequisites, the execution command or runner URL, and the results. The following cases are proposed. Confirm the expected fallback behaviour against the implemented solution.

| Scenario | Expected evidence |
| --- | --- |
| Source response contains a known car park | The integration maps the identifier, lot count, and source timestamp correctly. |
| The same source record is synchronised again | Repeating the sync leaves a single, consistent current availability result. |
| Available lots are zero | The UI shows zero or full without treating it as missing data. |
| No usable data or the last reading is old | The UI indicates that the reading is missing or stale. |
| Source API times out or returns an error | The user sees the actual fallback behaviour and an operator can locate the event. |
| A user looks up a known location | The application shows the matching car park and its availability. |

Use fixed fixtures for backend assertions where possible. Keep any smoke test that requires live data.gov.sg or a deployed OutSystems URL separate from the offline package checks. Runtime tests were unavailable during repository preparation.
