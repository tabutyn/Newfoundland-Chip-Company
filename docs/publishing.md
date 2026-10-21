# Publishing this starter on GitHub

Suggested repository name: **newfoundland-computers**. Suggested description:

> MIT-licensed plans for a Newfoundland semiconductor and computer industry: wafers, equipment, chip design and manufacturing, 2026–2056.

The archive contains the working documents and GitHub contribution templates. A GitHub repository exists only after it is created in an account and these files are pushed or uploaded. This guide does not claim that publication has happened.

## With Git and the GitHub CLI

Open the extracted `newfoundland-computers` directory. Check that the intended account is active:

```bash
gh auth status
```

If needed, use `gh auth login` and complete GitHub's normal authentication flow. Then initialize a local repository if it is not already initialized, use your normal Git author identity, and commit the files:

```bash
git init -b main
git add .
git commit -m "Add open Newfoundland semiconductor industry roadmap"
```

Create the public repository under the intended authenticated account and push:

```bash
gh repo create newfoundland-computers --public --source=. --remote=origin --push --description "MIT-licensed plans for a Newfoundland semiconductor and computer industry, 2026-2056."
```

The `--public` option matches the goal of an openly accessible plan. If that name is already taken in the account, choose a new name rather than overwrite an existing repository. Do not create a second README or license through GitHub; both are already included.

See the [official GitHub CLI create command](https://cli.github.com/manual/gh_repo_create) for current flags and account/organization behavior.

## With the GitHub website

Create a new repository, choose the account and repository name, select public visibility for the open plan, and leave automatic README/license/gitignore initialization off. Upload the **extracted file tree**, preserving `companies`, `docs`, `finance`, `research`, `templates`, `scripts`, and `.github`. Uploading only the ZIP will not give readers a browsable plan. Command-line Git is usually easier for preserving the contribution-template directory.

## After publication

1. Open the rendered README and follow the four company links.
2. Verify that GitHub recognizes the root MIT `LICENSE`.
3. Check that issue templates and the pull-request template appear.
4. Run `python3 scripts/capital_model.py` locally and compare the C$10.5–29M result.
5. Turn selected [backlog tasks](backlog.md) into issues, with an owner only after they accept.
6. Make the first public release after checking the evidence and budget snapshot. Do not describe the project as funded or endorsed.

Suggested topics, if useful: `newfoundland`, `semiconductors`, `open-hardware`, `economic-development`, `chip-design`, `manufacturing`. Topics describe the plan's subject; they do not imply that hardware designs or manufacturing facilities have already been delivered.
