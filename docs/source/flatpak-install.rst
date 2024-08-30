As a Flatpak
============

Prerequisites
-------------

* flatpak - Go `here <https://www.flatpak.org/setup/>`__, select your distro, and follow the directions to install flatpak.
* flatpak-builder - According to `here <https://docs.flatpak.org/en/latest/first-build.html>`__::

  ...[flatpak-builder] is usually available from the same repository as   the flatpak package (e.g. use apt or dnf). You can also install it as a flatpak with ``flatpak install flathub org.flatpak.Builder``.

Installation
------------

1. First of all, make sure you have the :ref:`above prerequisites    <flatpak-install:Prerequisites>`.
2. Download the latest "galaxy-flasher-version-os.zip" file from `the GitHub Releases page <https://github.com/ethical-haquer/Galaxy-Flasher/releases/>`_. It is a good idea to make a new directory and save the file there, to keep it more contained.
3. Once the file is downloaded, extract it.
4. Move into the newly extracted directory. It should be named the same as the file, minus the ".zip" part.
5. Move into the "flatpak" directory.
6. Run this command in the terminal::

  $ ./build.sh

You must be located in the same "flatpak" directory in the terminal when you run it. If you don't know how to change directories in the terminal, look at `this guide <https://itsfoss.com/change-directories/>`_.
7. If the command finishes with a lot of output, and you get no errors, then go to step 17. If you instead get "Failed to init: Unable to find sdk org.gnome.Sdk version 46", continue following the steps below.
8. Run "flatpak install org.gnome.Sdk" in the terminal. You should get a list of different versions to choose from.
9. Select version 46.
10. If what you see looks correct, type "y" and hit enter. Once it says "Changes complete.", continue.
11. Run this command again, from the "flatpak" directory::

  $ ./build.sh

12. Once again, if the command finishes with a lot of output, and you get no errors, then go to step 17. If you instead get "Failed to init: Unable to find runtime org.gnome.Platform version 46", continue following the steps below. (you're almost done!)
13. Run this command in the terminal::

  $ flatpak install org.gnome.Platform

You should get a list of different versions to choose from.
14. Select version 46.
15. If what you see looks correct, type "y" and hit enter. Once it says "Changes complete.", continue.
16. Run this command again, from the "flatpak" directory::

  $ ./build.sh

17. You've finished installing Galaxy Flasher, congratulations! Galaxy Flasher should now show up as an app. You can also run it from the terminal with::

  $ flatpak run com.ethicalhaquer.galaxyflasher

