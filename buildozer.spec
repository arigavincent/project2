[app]

# (str) Title of your application
title = Add Numbers App

# (str) Package name
package.name = addnumbersapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude any files)
source.exclude_exts = spec

# (list) List of exclusions using pattern matching
source.exclude_patterns = license,imagesourceatlas.json

# (str) Application version
version = 1.0

# (int) Minimum source code version
osx.python_version = 3

# (str) Pinned version
osx.kivy_version = 2.1.0

# (list) Application requirements
requirements = kivy

# (str) Custom source folders for requirements
# source.include_exts = .git, lib, buildozer
# source.include_patterns = README.md, LICENSE

# (list) Garden requirements
# garden_requirements = 

# (list) Old requirements without "kivy" or "python-for-android"
# requirements_old = sdl2, PIL, gevent

# (list) Permissions
# android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
# android.api = 27

# (int) Android SDK version to use
# android.sdk = 20

# (str) Android NDK version to use
# android.ndk = r19c

# (int) Android NDK API to use. This is the minimum API your app will work on.
# android.ndk_api = 21

# (int) iOS SDK version
# ios.sdk = 9.0

# (str) iOS build target (one of 'iphone' or 'ipad')
# ios.build_target = iphone

# (bool) Use the --private data flag
# android.private_storage = True

# (str) iOS deployment target
# ios.deployment_target = 10.0

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
# android.ndk_path = 

# (str) Android entry point
# android.entrypoint = org.renpy.android.PythonActivity

# (str) iOS entry point
# ios.entrypoint = 

# (list) List of categories (for iOS only)
# ios.categories = 

# (str) Application orientation (one of portrait, landscape or all)
# orientation = portrait

# (str) Kivy version to use
# osx.kivy_version = 1.10.1

# (bool) Set to 1 if you want this app to be fullscreen
# fullscreen = 0

# (str) Presplash of the application
# presplash.filename = %(source.dir)/data/presplash.png

# (str) Icon of the application
# icon.filename = %(source.dir)/data/icon.png

# (str) Supported orientations (for Android)
# orientation = portrait

# (str) OUYA
