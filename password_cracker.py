import hashlib
import string
import itertools
import time

# open the hashes.txt file and read the hashes into a list
with open('hashes.txt') as hashes_file:
	md5_hash_list = hashes_file.readlines()

# remove '\n' character at the end of each hash with a list comprehension
md5_hash_list = [x.strip() for x in md5_hash_list]

# verify list
print(md5_hash_list)
input('Press enter to continue...')

# open results file
results_file = open('results.txt', 'w')

counter = 0
string_length = 1

# iterate through loaded md5 hashes
for md5_hash in md5_hash_list:

	# start the timer
	start_time = time.time()
	is_solved = False

	for string_length in range(1, 10):
		if is_solved == True:
			break
		else:
			# user itertools.product() to generate strings
			for combo in itertools.product(string.ascii_letters + string.digits + string.punctuation, repeat=string_length):
				# make the candidate password string from the combo tuple
				candidate_password = ''.join(combo)
				# hash the candidate password
				candidate_password_hash = hashlib.md5(candidate_password.encode('UTF-8')).hexdigest()
			
				# print statement for tracking progress
				print(f'Working to crack: {md5_hash} | Iteration: {counter} | Length: {string_length} | Candidate: {candidate_password} | Candidate hash: {candidate_password_hash}')

				# increment the counter
				counter += 1

				# compare the candidate password hash to the loaded md5 hash
				if candidate_password_hash == md5_hash:
					print(f'Found a match! Hash: {md5_hash} is equivalent to the md5 hash of {candidate_password}, which is {candidate_password_hash}')
					time_taken = round(time.time() - start_time, 3)
					print(f'Time taken to find a match: {time_taken} seconds.')
					
					# save results to results.txt
					results_file.write(f'Found a match! Hash: {md5_hash} is equivalent to the md5 hash of {candidate_password}, which is {candidate_password_hash} \n')
					results_file.write(f'Time taken to find a match: {time_taken} seconds. \n \n')
					results_file.flush()

					# manually review matches
					input('Press enter to continue...')

					# reset string_length & counter and exit for loop, to move on to next md5 hash
					string_length = 0
					counter = 0
					is_solved = True
					break
				else:
					continue