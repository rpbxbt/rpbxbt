# Branch Protection Rules

This repository uses GitHub branch protection to keep the `main` branch stable. The recommended settings are:

- **Require pull requests** before merging.
- **Require at least one approving review.**
- **Require the `CI` status check to pass.**
- **Enforce for administrators** so everyone follows the same process.
- **Restrict direct pushes** to the `main` branch.

To apply these rules:

1. Open your repository on GitHub and go to **Settings** → **Branches**.
2. Click **Add rule** under "Branch protection rules".
3. For **Branch name pattern**, enter `main`.
4. Check **Require a pull request before merging** and set **Require approvals** to *1*.
5. Check **Require status checks to pass before merging** and select `CI`.
6. Enable **Include administrators**.
7. Save the rule.

These settings ensure all changes go through review and pass automated tests before reaching `main`.
