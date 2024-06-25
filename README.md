<div align="center">
    <img src="https://raw.githubusercontent.com/EmberLightVFX/test_old/main/assets/logo.svg?sanitize=true" alt="logo" title="Logo" height="250" />

# Camera Sensor Database
</div>

<p align="center">
  <i>A collection of camera sensor information. Free to use anywhere.</i>
</p>

<p align="center">
     <img alt="GitHub last commit (branch)" src="https://img.shields.io/github/last-commit/EmberLightVFX/test_old/main?color=48b293">
     <a href="https://github.com/EmberLightVFX/test_old/graphs/contributors">
          <img src="https://img.shields.io/github/contributors-anon/EmberLightVFX/test_old?color=d1a91d" alt="contributors"></a>
     <img alt="GitHub Issues or Pull Requests" src="https://img.shields.io/github/issues-pr/EmberLightVFX/test_old">
     <a href="https://ko-fi.com/E1E0ZQTGC">
          <img alt="Static Badge" src="https://img.shields.io/badge/donate-fa615d?logo=ko-fi&logoColor=white"></a>
     <img alt="GitHub License" src="https://img.shields.io/github/license/EmberLightVFX/test_old?color=097bbb">
</p>

<p align="center">
  <a href="#web-docs">Web Docs</a> •
  <a href="#external-projects">External Projects</a> •
  <a href="#data-structure">Data Structure</a> •
  <a href="#formats">Formats</a> •
  <a href="#missing-sensor-data">Missing Sensor Data?</a>
</p>

## Web Docs

You can browse all data directly in the browser here:

<https://emberlightvfx.github.io/Camera-Sensor-Database/>

## External Projects

This is a list of external projects using Camera Sensor Database:

* [Camera Sensor Database for BlackMagic Fusion](https://www.steakunderwater.com/wesuckless/viewtopic.php?p=49031#p49031)

## Data Structure

```cmd
Vendor
└─── Camera
     ├─── Info
     │    └─── Other
     └─── Sensor Dimensions
          ├─── Focal Length (optional)
          ├─── Resolution
          │    ├─── Height
          │    └─── Width
          ├─── mm
          │    ├─── Height
          │    ├─── Width
          │    └─── Diagonal
          └─── Inches
               ├─── Height
               ├─── Width
               └─── Diagonal
```

## Formats

The data comes in multiple formats.
You find them all in the data folder.

- json
- csv
- yaml
- markdown

## Missing Sensor Data?

To add a new sensor data, create a new sensor submission by going to [Issues -> New issue -> Sensor Submission](https://github.com/EmberLightVFX/Camera-Sensor-Database/issues/new/choose) and fill out all needed information.
After submitting a PR will automatically be created with all files auto-generated and ready to be reviewed.
