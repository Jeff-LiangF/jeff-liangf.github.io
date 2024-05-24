from moviepy.editor import VideoFileClip

def reduce_video_size(input_path, output_path, bitrate='1m'):
    # Load the video file
    clip = VideoFileClip(input_path)
    
    # Write the output file with a reduced bitrate and ensure audio is included
    clip.write_videofile(output_path, bitrate=bitrate, audio_codec='aac', audio_bitrate='128k')

# Specify the path to your input video and the output path for the compressed video
input_video_path = './streamv2v_video.mp4'
output_video_path = './streamv2v_video_downsize.mp4'

# Call the function to reduce the video size
reduce_video_size(input_video_path, output_video_path)