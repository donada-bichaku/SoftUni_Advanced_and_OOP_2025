from collections import deque

final_feed = []

suggested = deque(int(el) for el in input().split())
featured = [int(el) for el in input().split()]
target = int(input())

while suggested and featured:
    curr_sug = suggested.popleft()
    curr_fea = featured.pop()
    if curr_fea > curr_sug:
        identifier = "featured"
        remainder_found = curr_fea % curr_sug
    elif curr_sug > curr_fea:
        identifier = "suggested"
        remainder_found = curr_sug % curr_fea
    else:
        identifier = None
        final_feed.append(0)


    if identifier:
        double_reminder = remainder_found * 2
        if identifier == "featured":
            final_feed.append(abs(remainder_found))
            if double_reminder != 0:
                featured.append(double_reminder)
        elif identifier == "suggested":
            if remainder_found > 0:
                final_feed.append(remainder_found * (-1))
            else:
                final_feed.append(remainder_found)
            if double_reminder != 0:
                suggested.append(double_reminder)

total_engagement = sum(final_feed)

print(f"Final Feed: " + ", ".join(str(el) for el in final_feed))

if total_engagement >= target:
    print(f"Goal achieved! Engagement Value: {total_engagement}")
else:
    print(f"Goal not achieved! Short by: {target-total_engagement}")
