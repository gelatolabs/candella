#
# ASDefinitions.rpy
# Candella
#
# Created by Marquis Kurt on 6/30/19.
# Copyright © 2019 ProjectAliceDev. All rights reserved.
#

init -1000:

    # MARK: OS release definitions
    define AS_SYS_INFO = {
        "NAME": "ChadOS",
        "VERSION": "2095",
        "COMMON_NAME": "chadlet",
        "CHANNEL": "stable",
        "BUILD_ID": "GITHASH"
    }

    python:
        import json

        with renpy.file("System/release_info.json") as manifest:
            lsb_release = json.load(manifest)["distribution"]

        AS_SYS_INFO["NAME"] = lsb_release["name"]
        AS_SYS_INFO["VERSION"] = lsb_release["version"]
        AS_SYS_INFO["BUILD_ID"] = lsb_release["build_id"]
        AS_SYS_INFO["COMMON_NAME"] = lsb_release["codename"]
        AS_SYS_INFO["CHANNEL"] = lsb_release["channel"]

    # MARK: OS directory definitions
    # Define system-wide directories here. These definitions are used
    # to prevent re-typing common directory locations.
    define AS_SYSTEM_DIR = "System/"
    define AS_FRAMEWORKS_DIR = "System/Frameworks/"
    define AS_CORESERVICES_DIR = "System/CoreServices/"
    define AS_DEFAULT_APP_DIR = "System/Applications/"
    define AS_FONTS_DIR = "System/Library/Fonts/"
    define AS_APPS_DIR = "Applications/"
    define AS_LIBRARY_DIR = "System/Library/"

    init python:

        # Get the framework directory from the framework name. This function
        # is intended to prevent re-typing of framework locations for typical
        # AliceOS frameworks.
        def AS_FRAMEWORK_DIR(FRAMEWORK_NAME="Default"):
            return AS_FRAMEWORKS_DIR + FRAMEWORK_NAME + ".aosframework/"
