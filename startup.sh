echo "
============ ϻѧϲʜѧ υ𝒔ᴇʀʙο𝞽 ============
Starting Now...
Copyright (c) 2021 CALLMEVP | @Macha_Userbot
"

start_machaub () {
    if [[ -z "$PYRO_STR_SESSION" ]]
    then
	    echo "Please add Pyrogram String Session"
    else
	    python3 -m Macha-UB
    fi
  }

_install_machaub () {
    start_machaub
  }

_install_machaub
