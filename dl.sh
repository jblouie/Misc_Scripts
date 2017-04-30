#.bash_profile alias for easy use
#alias dl='sh dl.sh'



youtube-dl -q -o '~/Downloads/Temp_Music/%(title)s.%(ext)s' -x --audio-format mp3 $1 


#AppleScript Folder Action on Temp_Music Folder.
#Imports into iTunes and deletes the file
# on adding folder items to my_folder after receiving the_files
# 	repeat with i from 1 to number of items in the_files
# 		tell application "iTunes"
# 			launch
# 			try
# 				set this_file to (item i of the_files)
				
# 				add this_file
				
# 				(*
# 				-- if you have iTunes set to 
# 				--"Copy files to iTunes Music folder when adding to library"
# 				-- then you might want to delete the original file...
# 				-- if so, remove comments from this block and 
# 				-- use the UNIX commands below to delete the file
				
# 				set the file_path to the quoted form of the POSIX path of this_file
# 				do shell script ("rm -f " & file_path)
				
# 				*)

# 				set the file_path to the quoted form of the POSIX path of this_file
# 				do shell script ("rm -f " & file_path)

# 			end try
# 		end tell
# 	end repeat
# end adding folder items to