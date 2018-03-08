import sys

while True:
    nums = sys.stdin.readline().strip().split()
    print(abs(int(nums[0])-int(nums[1])))
