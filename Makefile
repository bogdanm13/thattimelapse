# This is not a Makefile

timestamp:=$(shell date +%s)
timelapse_dir:=capture/timelapse

test_camera:
	python3 camera.py

timelapse: save_previous do_timelapse generate_video
	echo "Done!"

upload:
	dropbox_uploader.sh upload $(timelapse_dir) /

save_previous:
	mv $(timelapse_dir) $(timelapse_dir)-$(timestamp)

do_timelapse:
	python3 timelapse.py

generate_video:
	echo "Pass!"
