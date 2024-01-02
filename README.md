# Prompt Case Runner

Evaluate recorded model responses against explicit text and JSON assertions.

Uses Python 3.10+ and its standard library only. No package installation, virtual
environment, external service, or network access is required.

## Run

```console
python -m prompts_tool --help
python -m prompts_tool examples/sample.json
python -m prompts_tool --check-fixtures fixtures/cases.jsonl
python generate_fixtures.py --count 20
python -m unittest discover -s tests -v
```

Run from this directory. The optional path defaults to `-`, which reads JSON from
stdin. Output is JSON or a fixture-check summary. Exit codes are 0 success,
1 file failure, and 2 invalid input. Examples and fixtures contain generated data.

Requires a recorded response string, contains/excludes lists, and optional json_keys. Text assertions are case-sensitive; JSON keys are checked only at object top level. Malformed recorded JSON fails requested key assertions. No live model request, judge model, semantic scoring, or provider benchmark is involved.

## Learning focus

User-directed personal AI/LLM/agent exploration. This is an independent concept exercise based on the modeled
roadmap. It makes no claim to be employer-owned or period-authentic production code.

## Structure

- `prompts_tool/core.py`: validated parsing, storage, or state transitions.
- `prompts_tool/cli.py`: JSON command interface.
- `prompts_tool/generate_fixtures.py`: original deterministic validation cases.
- `prompts_tool/fixture_check.py`: expected-output/error checks.
- `fixtures/cases.jsonl`: 294 generated cases, with explicit descriptions.
- `tests/`: independently selected boundaries and the complete corpus check.

Branches `feature/core`, `feature/cli`, `data/fixtures`, and `docs/usage` retain
snapshots; `main` contains the complete tool. Dates and provenance are also recorded
in TIMELINE.json. Many data cases share a scenario; they are not separate features.

Keep changes focused, use actual dates for new work, and add a regression test
for changed behavior. Licensed under [MIT](LICENSE).

[History and provenance](HISTORY.md).
