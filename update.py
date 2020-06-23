#!/usr/bin/python3

# EagleShell Updater Shortcut


# Main shortcut update function
def update_shortcut_main():

    # Function that imports update script
    def update_shortcut():
        from modules.settings.updates.update import update_main
        update_main()

    # Function that imports setup script
    def setup_shortcut():
        from setup import setup_main
        setup_main()

    update_shortcut()

    setup_shortcut()


update_shortcut_main()
