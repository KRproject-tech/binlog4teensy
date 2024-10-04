**Communication**

<a style="text-decoration: none" href="https://twitter.com/hogelungfish" target="_blank">
    <img src="https://img.shields.io/badge/twitter-%40hogelungfish-1da1f2.svg" alt="Twitter">
</a>
<p>

**Language**
<p>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/arduino/arduino-original-wordmark.svg"  width="60"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/matlab/matlab-original.svg" width="60"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original-wordmark.svg" width="60"/>
<p>

# BinLog4teensy
Sample code of the __Fast__ binary data logging for __Teensy 4.1__.

Binary file saved on a micro SD card is read by __MATLAB code__ in "./load binary/" or __Python code on Anaconda environments__ in "./load binary_Py/".


## Format

Data is written as short int (2 Bytes) in "DATA.LOG".

![image](https://user-images.githubusercontent.com/114337358/206899316-ff17f5a5-9f0d-494a-b434-a7b967445486.png)


## Arduino sketches
* __main.ino__    : main code
### Required library for arduino IDE
* __SdFat__
https://www.arduinolibraries.info/libraries/sd-fat

## Usage

* __Compile code__

Compile source code by Arduino IDE and write to Teensy 4.1 board.

"DATA.LOG" is generated in micro SD card on Teensy 4.1 board.

* __Read binary file__

Read the generated file by "./load binary/plot_data.m"
    
    
![図1](https://github.com/KRproject-tech/binlog4teensy/assets/114337358/21a76cfa-dd38-479f-8eed-3b45d9b0a3a4)
