Tabs
====

Log Tab
-------

The Log Tab displays the output from the flash-tool.
You are also able to enter flash-tool commands into the Log Tab, just as you would in the terminal.

Options Tab
The Options Tab is where you can set flash-tool specific options.

For Thor, the options are:
  
* T Flash - Writes the boot-loader of a working device to the SD card.
* EFS Clear - Wipes phone/network-related stuff from your device. It should NOT be used by normal users.
* Bootloader Update - I honestly have no idea what this does. Let me know if you do!
* Reset Flash Count - I believe this does what it sounds like it does, but I don't know when you'd ever use it. Please correct me if I'm wrong!

Keep in mind that setting options through the Log Tab is buggy currently, and you need to start an Odin session before you can set any options.

For Odin4, there are currently no options.
The "-V", "Validate home binary with pit file" option might be added if someone can tell me what it does.
  
Pit Tab
-------

The Pit Tab is just a placeholder currently.

Settings Tab
------------

The Settings Tab is where you can change Galaxy Flasher's settings.
Here is a list of them:

* Flash Tool - The flash-tool you would like Galaxy Flasher to use. The options are:
* Thor - An open-source flash-tool. The last update was almost a year ago, sadly.
* Odin4 - A proprietary, official Samsung flash-tool that was leaked.
* PyThor - An open-source flash-tool that is still in development. The only real reason to use it is if you plan on contributing to it.
   
You will have to restart Galaxy Flasher after changing this setting for it to apply.

* Theme - The theme you would like Galaxy Flasher to use. The options are:

    * System - Galaxy Flasher will attempt to use the system theme.
    * Light - Light theme.
    * Dark - Dark theme.

* Keep Log dark - Keeps the Log Tab dark, regardless of the theme.
    
* [Thor] Automatically select all partitions - This automatically selects all of the partitions from the files you select, instead of asking you what ones you would like to select. This only applies to Thor.
