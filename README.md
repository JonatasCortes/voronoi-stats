<h1 align="center">Welcome to Voronoi Stats</h1>

<p align="center">
  <img src="assets/stats_neon.svg" alt="Code Territory card" width="800">
</p>

<p align="center">
  <b>Your languages, repositories and weekly activity as an animated Voronoi map for your GitHub profile.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.12-3776AB?logo=python&logoColor=white" alt="Python 3.12">
  <img src="https://img.shields.io/badge/GitHub_Actions-automated-2088FF?logo=githubactions&logoColor=white" alt="GitHub Actions">
  <img src="https://img.shields.io/badge/themes-27-ff0055" alt="27 themes">
  <img src="https://img.shields.io/badge/dependencies-none-2ea44f" alt="No dependencies">
  <img src="https://img.shields.io/badge/output-SVG-FFB13B?logo=svg&logoColor=white" alt="SVG output">
</p>

---

Do you want a profile card that shows what you actually write, instead of a plain bar of percentages? Then you are in the right place!

Voronoi Stats reads your repositories and your activity from the GitHub API and draws a **territory map**: each programming language is a territory, each repository is a cell inside it, and the size of everything follows the amount of code. Next to the map, four line charts show your last 12 months of commits, pull requests, issues and reviews. The result is a single `.svg` file, regenerated automatically every day by a GitHub Action.

It is also as light as it can be: **plain Python, no external dependencies** (only the standard library).

## Table of Contents

- [🧭 How to Read the Card](#how-to-read-the-card)
- [🚀 How to Use](#how-to-use)
  - [Step 1: Copy the `voronoi-stats/` folder](#step-1-copy-the-voronoi-stats-folder)
  - [Step 2: Create the GitHub Actions workflow](#step-2-create-the-github-actions-workflow)
  - [Step 3: Add a `.gitignore`](#step-3-add-a-gitignore)
  - [Step 4: Create the access token](#step-4-create-the-access-token)
  - [Step 5: Save the token as a repository secret](#step-5-save-the-token-as-a-repository-secret)
  - [Step 6: Run the pipeline](#step-6-run-the-pipeline)
  - [Step 7: Show the card in your profile](#step-7-show-the-card-in-your-profile)
  - [Optional: run it on your computer](#optional-run-it-on-your-computer)
- [🛠️ Customization](#customization)
  - [What you can change](#what-you-can-change)
  - [Constants reference](#constants-reference)
- [🎨 Themes](#themes)
  - [1. Basic Colors](#1-basic-colors)
  - [2. Year Seasons](#2-year-seasons)
  - [3. Drinks](#3-drinks)
  - [4. Countries and Culture](#4-countries-and-culture)
  - [5. Classical UI](#5-classical-ui)
- [🩺 Troubleshooting](#troubleshooting)

---

## How to Read the Card

| What you see | What it means |
| --- | --- |
| **Territory** (a large colored region) | One programming language. The legend shows its color and its real share of your code. |
| **Territory area** | Bytes of code in that language. Small languages get a minimum of 2.5% of the area so they stay visible. |
| **Cell** (a piece inside a territory) | One repository, in that language. A repository that uses several languages appears once in each of its territories. |
| **Cell opacity** | How recent the last push was. The oldest push is the faintest, the newest is the strongest. It is measured in whole weeks, so it does not change every day. |
| **Pulsing dot** | The repository received a push in the last 90 days. |
| **Dim dot** | No recent activity. |
| **Lines on the right** | Weekly activity for the last 12 months: commits, pull requests, issues and reviews. The big number is the 12-month total, and the dot marks the current week. |
| **REPOS / STARS / FORKS** | Totals of the repositories used in the map. |

Some rules about the data:

- Only your **top 5 languages** get their own territory. All the others are grouped into **Other**.
- **Forks and archived repositories** are left out.
- **Private repositories** are only included if the token has the `repo` permission (see [Step 4](#step-4-create-the-access-token)).

<p align="right"><a href="#table-of-contents">⬆ back to top</a></p>

---

## How to Use

Follow the steps below in order. In the end you will have a card that updates itself every day, with no manual work.

> [!NOTE]
> Everything below happens in your **profile repository**, the special repository named exactly like your GitHub username (for example, `Bob/Bob`).

### Step 1: Copy the `voronoi-stats/` folder

See the `voronoi-stats/` folder in this repository? Copy the **entire folder** to the root of your profile repository.

### Step 2: Create the GitHub Actions workflow

Create a `.github/workflows` folder in the root of the repository and add a file called `voronoi-stats.yml` to it, with the following content:

```yml
name: voronoi-stats

on:
  schedule:
    - cron: "0 6 * * *"
  workflow_dispatch:

permissions:
  contents: write

concurrency:
  group: voronoi-stats
  cancel-in-progress: false

env:
  USERNAME: ${{ github.repository_owner }}
  THEME: neon

jobs:
  update:
    runs-on: ubuntu-latest
    steps:
      - name: Download repository
        uses: actions/checkout@v7

      - name: Install python
        uses: actions/setup-python@v6
        with:
          python-version: "3.12"

      - name: Generate svg card
        env:
          STATS_TOKEN: ${{ secrets.STATS_TOKEN }}
        run: python voronoi-stats/main.py "$USERNAME" --theme "$THEME"

      - name: Save to repository if changed
        run: |
          if [ -z "$(git status --porcelain assets/stats.svg)" ]; then
            echo "No updates were found."
          else
            git config user.name "github-actions[bot]"
            git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
            git add assets/stats.svg
            git commit -m "auto: update voronoi stats"
            git push
          fi
```

This workflow runs **every day at 06:00 UTC** and can also be started manually (`workflow_dispatch`). When something changes, it commits the new `assets/stats.svg` file by itself.

> [!WARNING]
> `USERNAME` defaults to the owner of the repository, which is correct for a profile repository. `THEME` accepts any of the names listed in the [Themes](#themes) section, so feel free to test all of them.

> [!NOTE]
> Python 3.12 is recommended. The code needs Python 3.9 or newer.

### Step 3: Add a `.gitignore`

You may also need a `.gitignore` file in the root of the repository, with at least the following lines:

```gitignore
__pycache__/
*.pyc
.DS_Store
```

### Step 4: Create the access token

The script needs permission to read your repositories and your activity. For that, create a **classic** personal access token:

1. Open **GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)**.
2. Click **Generate new token (classic)**.
3. Give it a name (for example, `voronoi-stats`) and select the `read:user` permission.
4. *(Optional)* If you want your **private repositories** in the map, also select `repo`. Without it, only public repositories are used.
5. Click **Generate token** and **copy it right away**, because GitHub will not show it again.

> [!IMPORTANT]
> Never commit the token to the repository. It must live only in the repository secrets, as shown in the next step.

> [!CAUTION]
> If the token expires, the automation will stop working, and a new token must be generated to restore functionality.

### Step 5: Save the token as a repository secret

With the token copied:

1. Go to your profile repository on GitHub and open **Settings → Secrets and variables → Actions**.
2. Click **New repository secret**.
3. In **Name**, type exactly `STATS_TOKEN`.
4. In **Secret**, paste the token you just created.
5. Click **Add secret**.

### Step 6: Run the pipeline

1. Open the **Actions** tab of the repository.
2. Select the **voronoi-stats** workflow.
3. Click **Run workflow**.

When the automation finishes, an `assets/` folder will be created with the `stats.svg` file inside it.

### Step 7: Show the card in your profile

Finally, add the following to your profile `README.md`:

```html
<p align="center">
  <a href="https://github.com/JonatasCortes/voronoi-stats">
    <img src="assets/stats.svg" alt="Code Territory" width="800">
  </a>
</p>
```

Set the `width` value that best suits your README, then **commit and push** the change.

> [!TIP]
> From now on you do not need to do anything else: the card will be refreshed every day automatically. 🎉

### Optional: run it on your computer

You can also generate the card locally, from the root of your profile repository:

```bash
# macOS / Linux
export GH_TOKEN="your_token_here"
python voronoi-stats/main.py YourGitHubUserName --theme neon
```

```powershell
# Windows (PowerShell)
$env:GH_TOKEN="your_token_here"
python voronoi-stats/main.py YourGitHubUserName --theme neon
```

The file is saved to `assets/stats.svg`.

<p align="right"><a href="#table-of-contents">⬆ back to top</a></p>

---

## Customization

Voronoi Stats was made to be adjusted to your taste, and there are two levels of customization.

### What you can change

| What | How | Where |
| --- | --- | --- |
| **Colors and visual style** | Pick a ready-made theme | `THEME` in the workflow → see [Themes](#themes) |
| **A new theme** | Add an entry to `THEMES` (name in lowercase, without spaces, `-` or `_`) | `voronoi-stats/themes.py` |
| **Anything else** (animation time, texts, sizes, opacity...) | Edit the constants | `voronoi-stats/constants.py` |

> [!NOTE]
> Any customization different from the ready-made [themes](#themes) must be done by modifying the file **`voronoi-stats/constants.py`**.

A theme does not choose the color of each language directly. Instead, it defines the **color range** the languages are picked from: a start hue, an end hue, a saturation and a lightness. The biggest language gets the start of the range, the smallest gets the end, and the others are spread in between. This way a green theme gives you green-ish languages, a purple theme gives you purple-ish ones, and so on.

In `constants.py` you can, for example, change how long the animation takes, translate every text of the card (title, legend, labels and number format) or change how many languages get their own territory.

### Constants reference

Here is what each group of constants is for:

| Group | Constants | What it controls |
| --- | --- | --- |
| **Texts** | `LABELS`, `THOUSANDS_SEP`, `DECIMAL_SEP`, `PERCENT_DECIMALS` | Every text of the card (title, legend, labels, accessibility description) and how numbers are written (`2,847` and `91.2%` by default) |
| **Data rules** | `MAX_LANGUAGES`, `OTHER_LABEL`, `MIN_AREA_SHARE`, `ACTIVE_DAYS`, `OPACITY_MIN`, `OPACITY_MAX` | How many languages get a territory, the minimum area of a territory, how long a repository counts as "active", and the opacity range of the cells |
| **Animation** | `ANIM_CELL_*`, `ANIM_TERRITORY_*`, `ANIM_SPARK_*`, `ANIM_NUM_*`, `ANIM_PULSE_*` | How long each part of the animation takes (in seconds) and when it starts |
| **Drawing** | `CELL_STROKE_W`, `TERRITORY_*`, `DOT_*`, `SPARK_*`, `GLOW_*`, `*_OPACITY` | Line thickness, dot sizes, background glow and the transparency of the small elements |
| **Typography** | `FONT_FAMILY`, `FONT_*` | The font and the size of every text |
| **Card layout** | `CARD_W`, `PAD`, `HEADER_*`, `PLOT_*`, `LEGEND_*`, `ACTIVITY_*`, `FOOTER_STATS_H` | The size of the card and the position and spacing of the map, the legend and the activity column |
| **Geometry** | `POWER_MAX_ITER`, `POWER_TOLERANCE`, `POWER_STEP`, `SEED_MARGIN`, `DOMINANT_SHARE` | How the map is calculated and how the biggest language is placed |
| **Output and GitHub API** | `OUTPUT_PATH`, `TOKEN_ENV`, `GRAPHQL_URL`, `REPOS_PAGE_SIZE`, `LANGS_PER_REPO` | Where the SVG is saved, the name of the token variable and how the data is requested from GitHub |

> [!TIP]
> The easiest and most noticeable changes are the animation times (`ANIM_*`) and `MAX_LANGUAGES`. Try `MAX_LANGUAGES = 3` for a cleaner map.

> [!CAUTION]
> Be careful with the **Card layout**, **Geometry** and **Output and GitHub API** groups. Changing them can misalign the card or break the data download. If something goes wrong, restore the original values. Also remember that:
> - if you change `ACTIVE_DAYS`, update the legend text in `LABELS` (`legend_active`), which says 90 days;
> - if you change `OUTPUT_PATH`, update the `git status` and `git add` paths in the workflow;
> - if you change `STATS_TOKEN`, update the `STATS_TOKEN` name in the workflow.

<p align="right"><a href="#table-of-contents">⬆ back to top</a></p>

---

## Themes

> [!NOTE]
> Theme names are not case sensitive, and spaces, hyphens (`-`) and underscores (`_`) are ignored. So `"japanlight"`, `"Japan-Light"` and `"JAPAN_LIGHT"` all select the same theme.

Jump straight to a block:

<table align="center">
  <thead>
    <tr>
      <th align="center">🎨 Basic Colors</th>
      <th align="center">🍂 Year Seasons</th>
      <th align="center">🍷 Drinks</th>
      <th align="center">🌍 Countries & Culture</th>
      <th align="center">💻 Classical UI</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center"><a href="#1-basic-colors"><b>Explore Themes ↗</b></a></td>
      <td align="center"><a href="#2-year-seasons"><b>Explore Themes ↗</b></a></td>
      <td align="center"><a href="#3-drinks"><b>Explore Themes ↗</b></a></td>
      <td align="center"><a href="#4-countries-and-culture"><b>Explore Themes ↗</b></a></td>
      <td align="center"><a href="#5-classical-ui"><b>Explore Themes ↗</b></a></td>
    </tr>
  </tbody>
</table>

### 1. Basic Colors

Simple, classic colors. Available themes: [`red`](#red) · [`orange`](#orange) · [`yellow`](#yellow) · [`green`](#green) · [`blue`](#blue) · [`purple`](#purple) · [`pink`](#pink)

#### Red

`--theme red`

<p align="center">
  <img src="assets/stats_red.svg" alt="Code Territory card, red theme" width="800">
</p>

#### Orange

`--theme orange`

<p align="center">
  <img src="assets/stats_orange.svg" alt="Code Territory card, orange theme" width="800">
</p>

#### Yellow

`--theme yellow`

<p align="center">
  <img src="assets/stats_yellow.svg" alt="Code Territory card, yellow theme" width="800">
</p>

#### Green

`--theme green`

<p align="center">
  <img src="assets/stats_green.svg" alt="Code Territory card, green theme" width="800">
</p>

#### Blue

`--theme blue`

<p align="center">
  <img src="assets/stats_blue.svg" alt="Code Territory card, blue theme" width="800">
</p>

#### Purple

`--theme purple`

<p align="center">
  <img src="assets/stats_purple.svg" alt="Code Territory card, purple theme" width="800">
</p>

#### Pink

`--theme pink`

<p align="center">
  <img src="assets/stats_pink.svg" alt="Code Territory card, pink theme" width="800">
</p>

<p align="right"><a href="#themes">⬆ back to themes</a></p>

---

### 2. Year Seasons

Softer, earthy palettes inspired by the four seasons. Available themes: [`spring`](#spring) · [`summer`](#summer) · [`autumn`](#autumn) · [`winter`](#winter)

#### Spring

`--theme spring`

<p align="center">
  <img src="assets/stats_spring.svg" alt="Code Territory card, spring theme" width="800">
</p>

#### Summer

`--theme summer`

<p align="center">
  <img src="assets/stats_summer.svg" alt="Code Territory card, summer theme" width="800">
</p>

#### Autumn

`--theme autumn`

<p align="center">
  <img src="assets/stats_autumn.svg" alt="Code Territory card, autumn theme" width="800">
</p>

#### Winter

`--theme winter`

<p align="center">
  <img src="assets/stats_winter.svg" alt="Code Territory card, winter theme" width="800">
</p>

<p align="right"><a href="#themes">⬆ back to themes</a></p>

---

### 3. Drinks

Warm tones inspired by classic drinks. Available themes: [`wine`](#wine) · [`beer`](#beer)

#### Wine

`--theme wine`

<p align="center">
  <img src="assets/stats_wine.svg" alt="Code Territory card, wine theme" width="800">
</p>

#### Beer

`--theme beer`

<p align="center">
  <img src="assets/stats_beer.svg" alt="Code Territory card, beer theme" width="800">
</p>

<p align="right"><a href="#themes">⬆ back to themes</a></p>

---

### 4. Countries and Culture

Colors inspired by flags and cultural symbols. Available themes: [`brazil`](#brazil) · [`usa`](#usa) · [`france`](#france) · [`india`](#india) · [`china`](#china) · [`japan`](#japan) · [`japanlight`](#japanlight) · [`sakura`](#sakura)

#### Brazil

`--theme brazil`

<p align="center">
  <img src="assets/stats_brazil.svg" alt="Code Territory card, brazil theme" width="800">
</p>

#### USA

`--theme usa`

<p align="center">
  <img src="assets/stats_usa.svg" alt="Code Territory card, usa theme" width="800">
</p>

#### France

`--theme france`

<p align="center">
  <img src="assets/stats_france.svg" alt="Code Territory card, france theme" width="800">
</p>

#### India

`--theme india`

<p align="center">
  <img src="assets/stats_india.svg" alt="Code Territory card, india theme" width="800">
</p>

#### China

`--theme china`

<p align="center">
  <img src="assets/stats_china.svg" alt="Code Territory card, china theme" width="800">
</p>

#### Japan

`--theme japan`

<p align="center">
  <img src="assets/stats_japan.svg" alt="Code Territory card, japan theme" width="800">
</p>

#### Japanlight

`--theme japanlight`

<p align="center">
  <img src="assets/stats_japanlight.svg" alt="Code Territory card, japanlight theme" width="800">
</p>

#### Sakura

`--theme sakura`

<p align="center">
  <img src="assets/stats_sakura.svg" alt="Code Territory card, sakura theme" width="800">
</p>

<p align="right"><a href="#themes">⬆ back to themes</a></p>

---

### 5. Classical UI

Popular palettes from well-known editors and interface styles, plus a few dramatic ones. Available themes: [`dracula`](#dracula) · [`mocha`](#mocha) · [`neon`](#neon) · [`atlas`](#atlas) · [`heaven`](#heaven) · [`hell`](#hell)

#### Dracula

`--theme dracula`

<p align="center">
  <img src="assets/stats_dracula.svg" alt="Code Territory card, dracula theme" width="800">
</p>

#### Mocha

`--theme mocha`

<p align="center">
  <img src="assets/stats_mocha.svg" alt="Code Territory card, mocha theme" width="800">
</p>

#### Neon

`--theme neon`

<p align="center">
  <img src="assets/stats_neon.svg" alt="Code Territory card, neon theme" width="800">
</p>

#### Atlas

`--theme atlas`

<p align="center">
  <img src="assets/stats_atlas.svg" alt="Code Territory card, atlas theme" width="800">
</p>

#### Heaven

`--theme heaven`

<p align="center">
  <img src="assets/stats_heaven.svg" alt="Code Territory card, heaven theme" width="800">
</p>

#### Hell

`--theme hell`

<p align="center">
  <img src="assets/stats_hell.svg" alt="Code Territory card, hell theme" width="800">
</p>

<p align="right"><a href="#themes">⬆ back to themes</a> · <a href="#table-of-contents">⬆ back to top</a></p>

---

## Troubleshooting

| Problem | What to check |
| --- | --- |
| **The workflow fails with "GitHub rejected the token"** | The token is wrong, expired or was revoked. Create a new one ([Step 4](#step-4-create-the-access-token)) and update the `CONTRIB_TOKEN` secret. |
| **"Environment variable GH_TOKEN is empty or missing"** | The secret is not named exactly `CONTRIB_TOKEN`, or the workflow does not pass it as `GH_TOKEN`. |
| **"GitHub user not found"** | The username is wrong. In a profile repository, `USERNAME` must be the account that owns it. |
| **"Theme ... not found"** | The `THEME` name does not exist. The error message lists every available theme. |
| **The workflow cannot push the SVG** | Open **Settings → Actions → General → Workflow permissions** and allow **Read and write permissions**. |
| **The card is empty or has few repositories** | Forks and archived repositories are ignored, and private repositories need the `repo` permission on the token. |
| **The card stopped updating after a long time** | GitHub can pause scheduled workflows in repositories with no activity for 60 days. Open the **Actions** tab and enable the workflow again, or run it manually. |

<p align="right"><a href="#table-of-contents">⬆ back to top</a></p>

---

<p align="center">
  Made with 💜 for GitHub profiles. If you liked it, leave a ⭐ on the repository!
</p>