print("📚 Study Planner")

# ---- INPUT SECTION ----
subject = input("Enter subject name: ")
days = int(input("Days until exam: "))
topics_count = int(input("Number of topics: "))

print("\nEnter topic names:")
topics = []

for i in range(topics_count):
    topics.append(input(f"Topic {i+1}: "))


# ---- PROCESSING ----
print("\nYour Study Plan:\n")

index = 0
plan_lines = []

for day in range(1, days + 1):
    if index < len(topics):
        line = f"📅 Day {day}: {topics[index]}"
        index += 1
    else:
        review_topic = topics[(day - len(topics) - 1) % len(topics)]
        line = f"📅 Day {day}: Review {review_topic}"

    print(line)
    plan_lines.append(line)


# ---- SAVE TO FILE ----
with open("study_plan.txt", "w", encoding="utf-8") as file:
    file.write(f"Study Plan for {subject}\n\n")
    for line in plan_lines:
        file.write(line + "\n")
print("\n✅ Study plan saved to study_plan.txt")        