km_run = (int(input('How many km did you run today ? ')))
target_km = (int(input('What is your target to run ? ')))
day = 1
while km_run < target_km:
    km_run *= 1.1
    day += 1
print('You will reach your target on ' + str(day) + ' day.')


# OR

# km_run = (int(input('How many km did you run today ? ')))
# target_km = (int(input('What is your target to run ? ')))
# day = 0
# track=[]
# track_sum=sum(track)
# while track_sum < target_km:
#     track.append(abs(int(km_run)))
#     km_run = km_run * 1.1
#     day = day + 1
#     print(track)
#     if track_sum > target_km:
#         break
# print('You will reach your target on ' + str(track_sum) + 'day.')