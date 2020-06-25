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

steps:
  - name: clone
    plugin: "gitclone"
    allow_failure: false

  - name: gen-report
    docker:
      image: node:12
    envs:
      NPM_CMD: "nyc report --reporter=html"
    plugin: 'npm-runner'

  - name: upload
    docker:
      image: ubuntu:18.04
    envs:
      REPORT_PATH: "${FLOWCI_GIT_REPO}/coverage"
      REPORT_NAME: "Code Coverage"
    plugin: 'report-upload'
```
