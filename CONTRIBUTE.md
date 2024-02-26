# Contribution

Hello! Follow the steps below to contribute to my repository. Also, in case of any questions, you can reach out to me on [Telegram](https://t.me/Giadissima1234).

## Pull Request Process

### Setting up the Repository

1) *Fork* the repository by clicking [here](https://github.com/Giadissima1/SortImages/fork).

2) Clone the repository by typing the following command:

   ```bash
   git clone https://github.com/Giadissima/SortImages
   ```

3. Connect your forked repository to mine:

   ```
   git remote add upstream https://github.com/Giadissima/SortImages
   ```

4. Verify the correct connection to my repository with the following command:

   ```bash
   git remote -v
   ```

> [!NOTE]
>
> You should have both "origin" (your fork) and "upstream" (the original repository).
>

5. (Optional) Create a new branch. Make sure you are in the right branch (e.g., the main branch) and create a new branch for your changes:

   ```bash
   git checkout -b nome-del-tuo-branch
   ```

6. Now you can run and modify the code.

### Running the Code

Find instructions in the [README.md](README.md) file.

### Creating a Pull Request

A Pull Request (**PR**) is a request to push your code to my repository. Once submitted, you'll need my approval for me to accept the changes to my repository. If I don't approve and you don't understand the reason, feel free to contact me. Follow these steps to create a PR:

- **Update the README.md** with details of the changes you made.

- **Increment version numbers in README.md** to the new version representing this Pull Request. The versioning scheme is [SemVer](https://semver.org/) (Major.Minor.Patch).

- **Ensure your code is up to date with mine on your repository**, if not, refer to the steps [below](https://github.com/Giadissima/SortImages/blob/main/CONTRIBUTE.md#updating-your-code-with-mine).

- **Push your changes to your fork on GitHub:**

  ```bash
  git push origin nome-del-tuo-branch
  ```

- **Create the PR on GitHub:**

  - Go to the main page of your repository on GitHub.
  - Switch to the branch you used to modify the code.
  - Click the "Pull Request" button and follow the instructions to create the PR.

- **Fill out the Pull Request form:** Provide a clear description of your changes in the Pull Request form. You can also mention any related issues.

- **Wait for the review.** I'll review your code as soon as possible, thanks for contributing ❤

### Updating Your Code with Mine

If I made changes after you forked the program, you won't be able to create a pull request. Here are the steps to update your code:

1. Ensure you have the latest version of my code by pulling:

   ```bash
   git pull upstream
   ```

2. Switch to your main branch (usually `main`):

   ```bash
   git checkout main
   ```

3. Merge the changes from my repository into your fork:

   ```bash
   git merge upstream/main
   ```

   Make sure to replace `main` with the name of your main branch if it's different.

4. Resolve any merging conflicts, if present.

5. Update your fork on your GitHub repository:

   ```bash
   git push origin main
   ```