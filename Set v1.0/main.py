#Import Required libraries
import time
import random
import pygame as pg
from pygame.locals import *
import set_shapes as ss
import time


#Initialize Variables---------------------------------------------------------------------------------------------------
#RBG Colors
red = (155, 0, 0)
green = (0, 155, 0)
blue = (0, 0, 155)
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (155, 155, 0)
purple = (75, 0, 155)
orange = (255, 128, 0)
pink = (255, 0, 255)
gray = (96, 96, 96)

#Card Characteristics
color_options = [red, green, blue]
shape_options = ['circle', 'square', 'triangle']
number_options = [1, 2, 3]
pattern_options = ['solid', 'hollow', 'striped']

#Display Variables
pg.init()
screen_width = 1200
screen_height = 705
screen_size = (screen_width, screen_height)
window_caption = 'SET the Game'
screen_title = 'SET'
background_color = white

#Fonts
title_font = pg.font.SysFont('consolas', 28, True, False)
header_font = pg.font.SysFont('consolas', 16, True, False)
normal_font = pg.font.SysFont('consolas', 16, False, False)

# Initialize the screen
pg.init()
screen = pg.display.set_mode(screen_size)
pg.display.set_caption(window_caption)

#Initialize Player info
p1_name = 'Player 1'
p1_pos = (50, 50)
p1_color = red

p2_name = 'Player 2'
p2_pos = (290, 50)
p2_color = blue

p3_name = 'Player 3'
p3_pos = (530, 50)
p3_color = green

p4_name = 'Player 4'
p4_pos = (770, 50)
p4_color = purple


#Initialize dictionaries of possible card combinations
def calc_possibilities(number=12):
    dict= {}
    counter = 0
    for i in range(number):
        for j in range(number):
            for k in range(number):
                if ([i, j, k] not in dict.values() and
                    [i, k, j] not in dict.values() and
                    [j, i, k] not in dict.values() and
                    [j, k, i] not in dict.values() and
                    [k, i, j] not in dict.values() and
                    [k, j, i] not in dict.values() and
                    i != j and i!= k and j != k):
                    dict[counter] = [i, j, k]
                    counter += 1
    return dict

dict_12 = calc_possibilities(12)
dict_9 = calc_possibilities(9)
dict_6 = calc_possibilities(6)



#Functions--------------------------------------------------------------------------------------------------------------
def print_message(font_style, msg_text, color=black, x=0, y=0):
    m = font_style.render(msg_text, True, color)
    screen.blit(m, [x, y])

def update_score(x, y, score, color=black):
    pg.draw.rect(screen, white, [x, y+20, 100, 30])
    value = header_font.render(str(score), True, color)
    screen.blit(value, [x, y+20])
    return "deal new cards"

def check_if_set(selected_cards):
    set_status = False
    shapes = False
    num_shapes = False
    colors = False
    patterns = False

    #Check to see if shapes are all the same or all different
    if (selected_cards[0].get_shape() == selected_cards[1].get_shape() and
        selected_cards[0].get_shape() == selected_cards[2].get_shape()):
        shapes = True
    elif (selected_cards[0].get_shape() != selected_cards[1].get_shape() and
          selected_cards[0].get_shape() != selected_cards[2].get_shape() and
          selected_cards[1].get_shape() != selected_cards[2].get_shape()):
        shapes = True

    #Check to see if numbers are all the same or all different
    if (selected_cards[0].get_number() == selected_cards[1].get_number() and
        selected_cards[0].get_number() == selected_cards[2].get_number()):
        num_shapes = True
    elif (selected_cards[0].get_number() != selected_cards[1].get_number() and
          selected_cards[0].get_number() != selected_cards[2].get_number() and
          selected_cards[1].get_number() != selected_cards[2].get_number()):
        num_shapes = True

    #Check if all colors are the same or all different
    if (selected_cards[0].get_color() == selected_cards[1].get_color() and
        selected_cards[0].get_color() == selected_cards[2].get_color()):
        colors = True
    elif (selected_cards[0].get_color() != selected_cards[1].get_color() and
          selected_cards[0].get_color() != selected_cards[2].get_color() and
          selected_cards[1].get_color() != selected_cards[2].get_color()):
        colors = True

    #Check if all the patterns are the same or all different
    if (selected_cards[0].get_pattern() == selected_cards[1].get_pattern() and
        selected_cards[0].get_pattern() == selected_cards[2].get_pattern()):
        patterns = True
    elif (selected_cards[0].get_pattern() != selected_cards[1].get_pattern() and
          selected_cards[0].get_pattern() != selected_cards[2].get_pattern() and
          selected_cards[1].get_pattern() != selected_cards[2].get_pattern()):
        patterns = True

    if shapes and num_shapes and colors and patterns:
        set_status = True
    else:
        set_status = False

    return set_status
    #End of check_if_set()

def draw_grid_lines():
    # vertical grid lines
    pg.draw.rect(screen, black, [0, 175, 3, screen_height - 175])
    pg.draw.rect(screen, black, [300, 175, 3, screen_height - 175])
    pg.draw.rect(screen, black, [600, 175, 3, screen_height - 175])
    pg.draw.rect(screen, black, [900, 175, 3, screen_height - 175])
    pg.draw.rect(screen, black, [1197, 175, 3, screen_height - 125])

    # horizontal grid lines
    pg.draw.rect(screen, black, [0, 175, screen_width, 3])
    pg.draw.rect(screen, black, [0, 350, screen_width, 3])
    pg.draw.rect(screen, black, [0, 525, screen_width, 3])
    pg.draw.rect(screen, black, [0, 703, screen_width, 3])

def print_instructions(string):
    #Display Message
    pg.draw.rect(screen, blue, [15, 140, 570, 30])
    print_message(header_font, string, white, 25, 145)

def print_alert(string):
    #Display Alert
    pg.draw.rect(screen, green, [630, 140, 250, 30])
    print_message(header_font, string, white, 640, 145)

def print_time(string):
    pg.draw.rect(screen, white, [5, 5, 250, 20])
    print_message(header_font, string, black, 10, 10)

def create_player_button(string, rect, colour):
    pg.draw.rect(screen, colour, [rect[0], rect[1], rect[2], rect[3]])
    print_message(header_font, string, white, rect[0]+10, rect[1]+8)



#Main Function----------------------------------------------------------------------------------------------------------
def main():
    #Initialize remaining variables

    # Initialize the set arrays
    selected_cards = []
    selected_cards_index = []
    cards_on_table = []
    grid_rectangles = []

    #Fill the deck "cards" where each card is unique (should be 81 cards total)
    cards = []
    for shape in shape_options:
        for number in number_options:
            for color in color_options:
                for pattern in pattern_options:
                    cards.append(ss.set_shapes(shape, number, color, pattern))

    #Initialize Player Scores
    p1_score = 0
    p2_score = 0
    p3_score = 0
    p4_score = 0

    #Get the number of cards remaining in the deck
    cards_remaining = len(cards)-12

    #Default Number of Players and Color, c
    num_players = 1
    c = red

    #Initialize the instructions message and the alert text
    message = "Look for a set of three cards."
    alert = ""

    #Button/Message Rectangles of the format [x, y, width, height]
    deal_card_button = [950, 140, 200, 30]
    check_for_sets_btn = [950, 90, 200, 30]
    one_player_btn = [100, 450, 100, 30]
    two_player_btn = [400, 450, 100, 30]
    three_player_btn = [700, 450, 100, 30]
    four_player_btn = [1000, 450, 100, 30]
    num_players_selected = [475, 500, 100, 50]
    restart_button = [950, 10, 200, 30]

    #Initialize Booleans/Loop Controls
    start_over = False
    is_set = True
    startGame = True
    printed = False
    current_status = "finding set"
    row = -1
    col = -1

    #Initialize the board-----------------------------------------------------------------------------------------------
    # Fill background
    background = pg.Surface(screen.get_size())
    background = background.convert()
    background.fill(white)
    screen.blit(background, (0, 0))

    #Open up the Welcome/Instruction screen.----------------------------------------------------------------------------
    while startGame:
        # Get the actions from the user
        for event in pg.event.get():
            #Only print the instructions/options once.
            if not printed:
                #Text for the instructions
                game_instructions1 = (
                    "The object of this game is to find a SET of 3 cards from 12 cards face up on the table. "
                    "Each card has four features:")
                game_instructions2 = ("1. Shape:   Circle, Square, or Triangle")
                game_instructions3 = ("2. Color:   Red, Blue, or Green")
                game_instructions4 = ("3. Number:  One, Two, or Three")
                game_instructions5 = ("4. Pattern: Solid, Striped, Hollow")
                game_instructions6 = (
                    "A SET consists of 3 cards in which each of the cards' features are the same on each card or different on each card.")
                game_instructions7 = (
                    "12 cards are dealt at a time. If a player finds a set, that player clicks on the three cards in the set. If it is a set,")
                game_instructions8 = (
                    "then that player gets a point. Click on the player name to add a point to that player. 3 new cards replace the 3 in the set.")
                game_instructions9 = (
                    "If there are no possible sets, you may click the 'Deal New Card' button to redeal 12 new cards.")
                game_instructions10 = (
                    "The game continues until there are no more cards in the deck and no more possible sets.")
                game_instructions11 = ("The player with the most points at the end of the game wins.")
                game_instructions12 = (
                    "Select the number of players and then press any button to begin the game. Good luck!")

                #Print the instruction text and format it
                print_message(title_font, "Welcome to SET", black, 500, 50)
                print_message(header_font, "Instructions:", black, 75, 75)
                print_message(normal_font, game_instructions1, black, 75, 100)
                print_message(normal_font, game_instructions2, black, 125, 125)
                print_message(normal_font, game_instructions3, black, 125, 150)
                print_message(normal_font, game_instructions4, black, 125, 175)
                print_message(normal_font, game_instructions5, black, 125, 200)
                print_message(normal_font, game_instructions6, black, 75, 225)
                print_message(normal_font, game_instructions7, black, 75, 250)
                print_message(normal_font, game_instructions8, black, 75, 275)
                print_message(normal_font, game_instructions9, black, 75, 300)
                print_message(normal_font, game_instructions10, black, 75, 325)
                print_message(normal_font, game_instructions11, black, 75, 350)
                print_message(normal_font, game_instructions12, black, 75, 375)

                #Create the buttons for selecting the number of players
                create_player_button("1 Player", one_player_btn, red)
                create_player_button("2 Players", two_player_btn, blue)
                create_player_button("3 Players", three_player_btn, green)
                create_player_button("4 Players", four_player_btn, purple)

                printed = True

            # Check what the user does. If the user presses any key, start the game
            if event.type == KEYDOWN:
                startGame = False
            #If the user selects the X in the top right, exit the program
            elif event.type == QUIT:
                exit()
            #Get the number of players for this game
            elif event.type == MOUSEBUTTONUP:
                mp = pg.mouse.get_pos()
                if (mp[0] > one_player_btn[0] and mp[0] < one_player_btn[0] + one_player_btn[2] and
                    mp[1] > one_player_btn[1] and mp[1] < one_player_btn[1] + one_player_btn[3]):
                    num_players = 1
                    c = red
                elif (mp[0] > two_player_btn[0] and mp[0] < two_player_btn[0] + two_player_btn[2] and
                    mp[1] > two_player_btn[1] and mp[1] < two_player_btn[1] + two_player_btn[3]):
                    num_players = 2
                    c = blue
                elif (mp[0] > three_player_btn[0] and mp[0] < three_player_btn[0] + three_player_btn[2] and
                    mp[1] > three_player_btn[1] and mp[1] < three_player_btn[1] + three_player_btn[3]):
                    num_players = 3
                    c = green
                elif (mp[0] > four_player_btn[0] and mp[0] < four_player_btn[0] + four_player_btn[2] and
                      mp[1] > four_player_btn[1] and mp[1] < four_player_btn[1] + four_player_btn[3]):
                    num_players = 4
                    c = purple
                #Print a message to the user letting him/her know what number of players have been selected
                (pg.draw.rect(screen, white, [num_players_selected[0], num_players_selected[1],
                                              num_players_selected[2]+300, num_players_selected[3]+100]))
                (print_message(title_font, str(num_players) + " Player Mode Selected", c,
                               num_players_selected[0], num_players_selected[1]))
        #Update the display
        pg.display.update()
        #End of Welcome/Instruction Screen -----------------------------------------------------------------------------


    #The user has pressed a key and is ready to play.

    #Create the game board and deal the first set of cards--------------------------------------------------------------
        #create 12 rectangles that can be used to cover up spots in grid
        #0(0,175)---1(300,175)---2(600,175)---3(900,175)----(1200,175)
        #4(0,350)---5(300,350)---6(600,350)---7(900,350)----(1200,350)
        #8(0,525)---9(300,525)---10(600,525)---11(900,525)--(1200,525)
        #b(0,700)----(300,700)----(600,700)----(900,700)----(122,700)
    pg.draw.rect(screen, white, [0, 0, screen_width, screen_height])
    for i in range(0, 3):
        for j in range(0, 4):
            grid_rectangles.append(pg.Rect(j*300+3, 175+i*175+3, 294, 169))

    #Deal the first set of cards
    for rectangle in grid_rectangles:
        pg.draw.rect(screen, white, rectangle)
        card_num = random.randint(0, len(cards)-1)
        cards[card_num].create_shape(screen, rectangle.x, rectangle.y)
        cards_on_table.append(cards[card_num])
        del cards[card_num]

    #Draw grid lines
    draw_grid_lines()

    # Display Title
    print_message(title_font, screen_title, black, 600, 10)

    #Display Deal New Cards
    pg.draw.rect(screen, red, deal_card_button)
    print_message(header_font, "Deal New Cards", white, deal_card_button[0]+40, deal_card_button[1]+6)

    #Display Check for Sets
    pg.draw.rect(screen, red, check_for_sets_btn)
    print_message(header_font, "Check if any sets", white, check_for_sets_btn[0]+27, check_for_sets_btn[1]+6)

    #Display Restart Button
    pg.draw.rect(screen, black, restart_button)
    print_message(header_font, "Restart Game", (255, 0, 0), restart_button[0]+45, restart_button[1]+6)

    # Display Player Info
    #Player 1
    print_message(header_font, p1_name, p1_color, p1_pos[0], p1_pos[1])
    update_score(p1_pos[0], p1_pos[1], p1_score, p1_color)
    #Player 2
    if num_players > 1:
        print_message(header_font, p2_name, p2_color, p2_pos[0], p2_pos[1])
        update_score(p2_pos[0], p2_pos[1], p2_score, p2_color)
    #Player 3
    if num_players > 2:
        print_message(header_font, p3_name, p3_color, p3_pos[0], p3_pos[1])
        update_score(p3_pos[0], p3_pos[1], p3_score, p3_color)
    #Player 4
    if num_players > 3:
        print_message(header_font, p4_name, p4_color, p4_pos[0], p4_pos[1])
        update_score(p4_pos[0], p4_pos[1], p4_score, p4_color)

    # Display Card Info
    print_message(header_font, "Cards Remaining", black, 980, 50)
    print_message(header_font, str(cards_remaining), black, 1038, 70)

    #Display Instructions
    print_message(header_font, "Instructions", blue, 15, 120)
    print_instructions(message)

    #Display Alert
    print_message(header_font, "Information", green, 630, 120)
    print_alert(alert)


    # Blit everything to the screen
    pg.display.update()

    #End of creating the game board-------------------------------------------------------------------------------------

    #Set the initial time for the timer
    t = time.time()
    sec = 0
    min = 0
    hour = 0
    timer = ""

    #-------------------------------------------------------------------------------------------------------------------
    #Playing the game Event Loop----------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------
    continueGame = True #Set to false when ready to exit the while loop
    while continueGame:

        #Print and increment the time every second----------------------------------------------------------------------
        if time.time() - t >= 1:
            t = time.time()
            if sec < 10 and min < 10:
                timer = ("Time: 0" + str(hour) + ":0" + str(min) + ":0" + str(sec))
            elif sec < 10 and min >= 10:
                timer = ("Time: 0" + str(hour) + ":" + str(min) + ":0" + str(sec))
            elif sec >= 10 and min < 10:
                timer = ("Time: 0" + str(hour) + ":0" + str(min) + ":" + str(sec))
            else:
                timer = ("Time: 0" + str(hour) + ":" + str(min) + ":" + str(sec))

            if sec < 59:
                sec += 1
            else:
                sec = 0

            if min < 59 and sec == 0:
                min += 1
            elif min == 60:
                min = 0
                hour += 1
            print_time(timer)
        #End of timer---------------------------------------------------------------------------------------------------

        # Determine message to print to screen and print it
        if current_status == 'finding set':
            message = "Look for a set of three cards."
        elif current_status == 'assign points':
            message = "Click on a player's name to give him/her a point."
        print_instructions(message)
        print_alert(alert)

        #Get the actions from the user
        for event in pg.event.get():

            # Check to see if the user clicks the exit button
            if event.type == QUIT:
                continueGame = False

            #When the user clicks, get the mouse position and do things
            elif event.type == MOUSEBUTTONUP:
                mouse_position = pg.mouse.get_pos()

                #If the user selects the Restart Button, exit the game loop and rerun Main() (which re-initializes
                #everything and starts back at the Welcome screen)
                if (mouse_position[0] < restart_button[0]+restart_button[2] and mouse_position[0] > restart_button[0] and
                    mouse_position[1] < restart_button[1]+restart_button[3] and mouse_position[1] > restart_button[1]):
                    start_over = True
                    continueGame = False

                #If you are currently looking for a set still
                if current_status == 'finding set': #------------------------------------------------------------------
                    if alert == "Not a set." or "Found a set!":
                        alert = ""

                    #Redeal all cards on the table----------------------------------------------------------------------
                    if (mouse_position[0] < (deal_card_button[0]+deal_card_button[2]) and mouse_position[0] > deal_card_button[0] and
                        mouse_position[1] < deal_card_button[1]+deal_card_button[3] and mouse_position[1] > deal_card_button[1]):
                        # Put cards on table back in the deck
                        if len(cards) >= 3:
                            for card in cards_on_table:
                                cards.append(card)

                            # Delete the cards on table
                            del cards_on_table[0:len(cards_on_table)]

                            # Re-deal
                            for rectangle in grid_rectangles:
                                pg.draw.rect(screen, white, rectangle)
                                card_num = random.randint(0, len(cards)-1)
                                cards[card_num].create_shape(screen, rectangle.x, rectangle.y)
                                cards_on_table.append(cards[card_num])
                                del cards[card_num]
                    #End of redealing all cards-------------------------------------------------------------------------

                    #Check if there are any sets on the table-----------------------------------------------------------
                    if (mouse_position[0] < (check_for_sets_btn[0]+check_for_sets_btn[2]) and mouse_position[0] > check_for_sets_btn[0] and
                        mouse_position[1] < check_for_sets_btn[1]+check_for_sets_btn[3] and mouse_position[1] > check_for_sets_btn[1]):
                        num_sets = 0
                        if len(cards_on_table) == 12:
                            for k, v in dict_12.items():
                                if check_if_set([cards_on_table[v[0]], cards_on_table[v[1]], cards_on_table[v[2]]]):
                                    num_sets += 1
                        elif len(cards_on_table) == 9:
                            for k, v in dict_9.items():
                                if check_if_set([cards_on_table[v[0]], cards_on_table[v[1]], cards_on_table[v[2]]]):
                                    num_sets += 1
                        elif len(cards_on_table) == 6:
                            for k, v in dict_6.items():
                                if check_if_set([cards_on_table[v[0]], cards_on_table[v[1]], cards_on_table[v[2]]]):
                                    num_sets += 1
                        if num_sets == 1:
                            alert = "There is 1 possible set."
                        else:
                            alert = "There are " + str(num_sets) + " possible sets."
                    #End of checking if there are any sets on the table ------------------------------------------------

                    #Get the column that was selected
                    if mouse_position[0] < 300:
                        col = 0
                    elif mouse_position[0] < 600:
                        col = 1
                    elif mouse_position[0] < 900:
                        col = 2
                    elif mouse_position[0] < 1200:
                        col = 3
                    #Get the row that was selected
                    if mouse_position[1] > 175 and mouse_position[1] < 350:
                        row = 0
                    elif mouse_position[1] > 350 and mouse_position[1] < 525:
                        row = 1
                    elif mouse_position[1] > 525 and mouse_position[1] < 700:
                        row = 2
                    #If the row and column were selected, add the selected cards to the array to check. Check for
                    #duplicate cards selected. If the card has been selected, alert the user.
                    if row >= 0 and col >= 0 and len(selected_cards) == 0:
                        selected_cards.append(cards_on_table[int(4 * row + col)])
                        selected_cards_index.append(int(4 * row + col))
                        row = -1
                        col = -1
                    elif row >= 0 and col >= 0 and (int(4 * row + col)) not in selected_cards_index:
                        selected_cards.append(cards_on_table[int(4 * row + col)])
                        selected_cards_index.append(int(4 * row + col))
                        row = -1
                        col = -1
                    elif (int(4 * row + col)) in selected_cards_index:
                        alert = "Card already selected."
                        message = "Instructions: Please pick a different card."

                    #Once three unique cards have been selected, check if it's a set
                    if len(selected_cards) == 3:
                        is_set = check_if_set(selected_cards)

                        #Alert the user if it's not a set and reset the selected_cards aray
                        if is_set == False:
                            alert = "Not a set."
                            del selected_cards[0:3]
                            del selected_cards_index[0:3]

                        #If the selected cards are a set, add points to the selected player and deal 3 new cards
                        elif is_set:
                            alert = "Found a set!"
                            current_status = "assign points"
                            continue
                #End of 'finding set'-----------------------------------------------------------------------------------

                if current_status == "assign points": #-----------------------------------------------------------------
                    #Select the player to add points to.
                    if (mouse_position[0] < 200 and mouse_position[1] < 150 and mouse_position[1] < 150
                            or num_players == 1):
                        p1_score += 1
                        current_status = update_score(p1_pos[0], p1_pos[1], p1_score, p1_color)
                    elif (mouse_position[0] >= 290 and mouse_position[0] < 440 and mouse_position[1] < 150
                            and num_players > 1):
                        p2_score += 1
                        current_status = update_score(p2_pos[0], p2_pos[1], p2_score, p2_color)
                    elif (mouse_position[0] >= 530 and mouse_position[0] < 680 and mouse_position[1] < 150
                            and num_players > 2):
                        p3_score += 1
                        current_status = update_score(p3_pos[0], p3_pos[1], p3_score, p3_color)
                    elif (mouse_position[0] >= 770 and mouse_position[0] < 920 and mouse_position[1] < 150
                            and num_players > 3):
                        p4_score += 1
                        current_status = update_score(p4_pos[0], p4_pos[1], p4_score, p4_color)
                #End of 'assign points'---------------------------------------------------------------------------------

                if current_status == "deal new cards": #----------------------------------------------------------------
                    #If it is a set, replace the three cards and subtract three from the cards_remaining
                    if cards_remaining > 2:# and is_set:
                        cards_remaining -= 3
                        pg.draw.rect(screen, white, [1010, 70, 150, 15])

                        #Deal new cards
                        for index in selected_cards_index:
                            pg.draw.rect(screen, white, grid_rectangles[index])
                            card_num = random.randint(0, len(cards)-1)
                            cards[card_num].create_shape(screen, grid_rectangles[index].x, grid_rectangles[index].y)
                            cards_on_table[index] = cards[card_num]
                            del cards[card_num]
                        print_message(header_font, str(len(cards)), black, 1010, 70)
                        alert = "3 new cards were dealt."

                    else:
                        alert = "No cards left in deck."
                        for index in selected_cards_index:
                            pg.draw.rect(screen, white, grid_rectangles[index])
                            del cards_on_table[index]
                    is_set = False
                    del selected_cards[0:3]
                    del selected_cards_index[0:3]
                    current_status = "finding set"
                #End of 'deal new cards'--------------------------------------------------------------------------------

        pg.display.update()
        #End of Game Event Loop-----------------------------------------------------------------------------------------

    return start_over
    #End of main()
    #If start_over = False then the game closes. If it is True, then the game will restart.


if __name__ == '__main__':
    replay = True
    while replay:
        #If the player selects to restart game, then replay will equal True and main will be called again until the game
        #ends without the player selecting to restart.
        replay = main()
