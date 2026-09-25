[app]

title = Snake
package.name = snake
package.domain = org.brenninhotools

source.dir = .
source.include_exts = py,png,jpg,kv,atlas
source.include_patterns = assets/*, src/*

version = 0.1

icon.filename = assets/images/icon.png

orientation = portrait

osx.python_version = 3
osx.kivy_version = 1.9.1

fullscreen = 1

requirements = python3,kivy

presplash.filename = %(icon.filename)s

android.permissions = INTERNET

android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a

android.allow_backup = True

[buildozer]

log_level = 2
warn_on_root = 1
