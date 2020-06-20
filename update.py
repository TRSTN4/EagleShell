#!/usr/bin/python3

# EagleShell Updater Shortcut


# Main shortcut update function
def update_shortcut_main():

    # Function that imports update script
    def update_shortcut():
        from modules.settings.updates.update import update_main
        update_main()

    update_shortcut()


update_shortcut_main()
