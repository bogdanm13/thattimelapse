# This is not a Makefile

timestamp:=$(shell date +%s)
timelapse_dir:=capture/timelapse
dropbox_dir:=/mnt/media/sync/Dropbox/Apps/thattimelapse/timelapse

test_camera:
	python3 camera.py

timelapse: save_previous do_timelapse upload
	echo "Done!"

upload:
	dropbox_uploader.sh upload $(timelapse_dir) /timelapse-$(timestamp)

save_previous:
	mv $(timelapse_dir) $(timelapse_dir)-$(timestamp)

do_timelapse:
	python3 timelapse.py capture --count=100

generate_video:
	# r - output framerate; 1 image -> 2 seconds = 50 frames
	ffmpeg -r 2 -i $(dropbox_dir)/timelapse_%01d.jpg -c:v libx264 -vf "fps=25,format=yuv420p" capture/timelapse.mp4
