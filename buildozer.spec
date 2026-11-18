[app]
title = MORGATHIS MANAGER
package.name = morgathismanager
package.domain = org.morgathis
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt
version = 0.1.0
requirements = python3,kivy==2.3.1
orientation = portrait
fullscreen = 0
android.permissions = INTERNET,ACCESS_NETWORK_STATE
android.api = 34
android.minapi = 23
android.archs = arm64-v8a
android.allow_backup = False
android.enable_androidx = True

[buildozer]
log_level = 2
warn_on_root = 1
