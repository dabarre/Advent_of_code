



def count_score(input_filename):
    
    score = 0

    with open(input_filename) as f_strategy:
        for turn in f_strategy.readlines():
            if turn.strip() == '': continue
            
            turn_split = turn.strip().split(' ')
            elf_play = ord(turn_split[0]) - ord('A')
            my_play = ord(turn_split[1]) - ord('X')

            outcome = (elf_play - my_play) % 3

            # Loss sum 0
        
            if outcome == 2:
                # Win
                score += 6
            elif outcome == 0:
                # Draw
                score += 3
                      
            # Bonus points always give at least 1
            score += my_play + 1
                
    return score

def count_score_secret_strategy(input_filename):
    
    score = 0

    with open(input_filename) as f_strategy:
        for turn in f_strategy.readlines():
            if turn.strip() == '': continue
            
            turn_split = turn.strip().split(' ')
            elf_play = ord(turn_split[0]) - ord('A')
            
            outcome = ord(turn_split[1]) - ord('X')
            my_play = (elf_play + outcome - 1) % 3

            # Loss sum 0

            if outcome == 2:
                score += 6
            elif outcome == 1:
                score += 3
            
            
            # Bonus points always give at least 1
            score += my_play + 1
                
    return score




def main():
    # Excercise 1
    score = count_score('day_2_data.txt')
    print(score)
    score_st = count_score_secret_strategy('day_2_data.txt')
    print(score_st)

if __name__ == "__main__":
    main()