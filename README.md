# report-upload

## Description

Upload report for job

## Inputs

- `REPORT_PATH`: the report path to upload, for example `${FLOWCI_GIT_REPO}/.coverage`
- `REPORT_NAME`: the report name that shown in job detail page
- `REPORT_CONTENT_TYPE` (optional): type could be `html`, `xml` or `json`, default type is `html`
- `REPORT_ENTRY_FILE` (optional): the entry file of report, default is `index.html`

## How to use it

```yml
envs:
  FLOWCI_GIT_URL: "https://github.com/hexojs/hexo.git"
  FLOWCI_GIT_BRANCH: "master"
  FLOWCI_GIT_REPO: "hexo"

steps:
  - name: clone
    plugin: "gitclone"
    allow_failure: false

  - name: npm install
    docker: # optional, can be run from node:12 image
      image: node:12
    envs:
      NPM_CMD: "npm install"
    plugin: "npm-runner"
```

## Screenshot

### nyc test coverage report

![](https://raw.githubusercontent.com/flowci-plugins/npm-runner/master/screenshot/report.png)
