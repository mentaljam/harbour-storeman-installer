[Unit]
Description=timer unit to trigger the unit for installing harbour-storeman

[Timer]
# Starts the corresponding service unit 1 - 2 seconds after activation:
OnActiveSec=1
AccuracySec=1
# Allows for retriggering without rebooting:
RemainAfterElapse=false
#Unit=harbour-storeman-installer.service
