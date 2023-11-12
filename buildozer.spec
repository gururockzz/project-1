# Buildozer configuration file

# Application details
[app]

# Title of your application
title = My Application

# Package name
package.name = myapp

# Package domain (needed for android/ios packaging)
package.domain = org.test

# Source code directory
source.dir = .

# List of source files to include
source.include_exts = py,png,jpg,kv,atlas

# Application version
version = 0.1

# Application requirements (comma-separated)
requirements = python3,kivy,kivymd,speechrecognition,pyttsx3

# Supported orientations (one of landscape, portrait, portrait-reverse, or landscape-reverse)
orientation = portrait

# Android-specific settings
[buildozer]

# Log level (0 = error only, 1 = info, 2 = debug with command output)
log_level = 2

# Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# Path to build artifact storage (absolute or relative to the spec file)
build_dir = ./.buildozer

# Path to build output storage (i.e., .apk, .aab, .ipa)
bin_dir = ./bin

# Android-specific settings
[app:android]

# Fullscreen setting (0 = False, 1 = True)
fullscreen = 0

# Supported architectures to build for
archs = arm64-v8a, armeabi-v7a

# Android API to target
api = 31

# Minimum API version supported
minapi = 21

# Android NDK version to use
ndk = 23b

# Android NDK API version to use
ndk_api = 21

# Application permissions
# Add android.permission.WRITE_EXTERNAL_STORAGE only if needed
permissions = INTERNET,WRITE_EXTERNAL_STORAGE

# Android-specific features
# Uncomment and customize if needed
#features = android.hardware.usb.host

# Android-specific dependencies to add
# Uncomment and customize if needed
#gradle_dependencies = com.example:example-library:1.0.0

# Android-specific logcat filters
# Uncomment and customize if needed
#logcat_filters = *:S python:D

# Android-specific additional adb arguments
# Uncomment and customize if needed
#adb_args = -H host.docker.internal

# Android-specific copy library setting (0 = False, 1 = True)
#copy_libs = 1

# iOS-specific settings (if needed)
# Uncomment and customize if building for iOS
#[app:ios]
#kivy_ios_dir = ../kivy-ios
#kivy_ios_url = https://github.com/kivy/kivy-ios
#kivy_ios_branch = master
#codesign.allowed = false
#codesign.debug = "iPhone Developer: <lastname> <firstname> (<hexstring>)"
#codesign.development_team.debug = <hexstring>

# Profiles (if needed)
# Uncomment and customize if using profiles
#[app@demo]
#title = My Application (demo)
#[app:source.exclude_patterns@demo]
#images/hd/*

