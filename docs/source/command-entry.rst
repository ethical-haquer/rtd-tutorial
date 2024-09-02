Command Entry
=============

| The Command Entry is somewhere you can enter flash-tool commands.
| If you read about :doc:`the Log Tab <log-tab>`, you might be wondering why it is needed if you can just type commands directly into the Log Tab.

| The reason is, commands entered into the Log Tab will not be made graphical. That means if you type "connect" into the Log Tab, you will have to select a device in the terminal. If you type "connect" into the Command Entry, Galaxy Flasher will either display a window asking you what device you want to connect to, or, if there is only one device, it will automatically select it. In other words, typing "connect" in the Command Entry does the same thing as clicking the Connect Button.

| Currently, only the "connect" and "flashTar" commands behave differently when sent through the Command Entry:

* **connect** - Behaves the same as hitting the Connect Button.
* **flashTar** - Behaves the same as hitting the Flash Button. The command entered must be just "flashTar" though. For example, running "flashTar /home/name/folder" will not do this.
