def output(labelDict):
    # for optimism and pecimism
    msg = []
    if labelDict["Optimism"]==labelDict["Pecimism"] and labelDict["Pecimism"]!=0:
        msg.append("You can be Optimistic and Pecimistic depending on the situation, we can say that there is a balance in your approch.")
    elif labelDict["Optimism"]==0 and labelDict["Pecimism"]==0:
        msg.append("You are neither Optimistic nor Pecimistic.")
    elif labelDict["Pecimism"]==0:
        if labelDict["Optimism"]==3:
            msg.append("Your approach towards your surrounding is very Optimistic.")
        elif labelDict["Optimism"]==2:
            msg.append("You are quite Optimistic in nature.")
        elif labelDict["Optimism"]==1:
            msg.append("You are a bit towards Optimistic side.")
    elif labelDict["Pecimism"]==1:
        if labelDict["Optimism"]==3:
            msg.append("Your approach is most of the time quite Optimistic while occasionally Pecimistic.")
        elif labelDict["Optimism"]==2:
            msg.append("You are usually Optimistic in nature but sometimes Pecimist.")
        elif labelDict["Optimism"]==0:
            msg.append("You are a bit Pecimistic.")
    elif labelDict["Pecimism"]==2:
        if labelDict["Optimism"]==3:
            msg.append("Your approach is usually Optimistic but sometimes Pecimistic.")
        elif labelDict["Optimism"]==1:
            msg.append("You are usually Pecimistic in nature but sometimes Optimist.")
        elif labelDict["Optimism"]==0:
            msg.append("You are quite Pecimistic in nature.")
    elif labelDict["Pecimism"]==3:
        if labelDict["Optimism"]==2:
            msg.append("Your approach is usually Pecimistic but sometimes Optimistic.")
        elif labelDict["Optimism"]==1:
            msg.append("Your approach is most of the time quite Pecimistic while occasionally Optimistic.")
        elif labelDict["Optimism"]==0:
            msg.append("Your approach towards your surrounding is very Pecimistic.")
    
    # for depression and joy
    if labelDict["Depression"]==3:
        if labelDict["Joy"]==2:
            msg.append("You are depressed but not sad and still enjoy and stay cheerful.")
        elif labelDict["Joy"]==1:
            msg.append("You are depressed and try to overcome it by little Joy around you.")
        elif labelDict["Joy"]==0:
            msg.append("Your handwriting reveals you are very Depressed.")
    elif labelDict["Depression"] in (1,2):
        if labelDict["Joy"]==2:
            msg.append("You sometimes get Depressed but handle it quite well and stay Cheerful.")
        elif labelDict["Joy"]==1:
            msg.append("You sometimes are Depressed but still Happy.")
        elif labelDict["Joy"]==0:
            msg.append("You seem to be under Depression.")
    elif labelDict["Depression"]==0:
        if labelDict["Joy"] in (1,2):
            msg.append("You are always Happy and Cheerful.")
        elif labelDict["Joy"]==0:
            msg.append("You don't feel much Joy, you are just doing things.")
    
    # for fear
    if labelDict["Fear"]==2:
        msg.append("You Fear very much about the outcomes of your action.")
    elif labelDict["Fear"]==1:
        msg.append("You Fear a bit about what is to be done.")
    elif labelDict["Fear"]==0:
        msg.append("You don't Fear much and try to be calm in unexpected situations.")
    
    # for goal oriented
    if labelDict["Goal Oriented"]==1:
        msg.append("You tend to focus on your Goals and achieve them.")
    elif labelDict["Goal Oriented"]==-1:
        msg.append("Can not focus on a single task at a time, thus are not Goal oriented.")
    """elif labelDict["Goal Oriented"]==0:
        msg.append("Can't say anything about this")"""
    
    # for self esteem and others value
    if labelDict["Self Esteem"]==3:
        if labelDict["Others Value"]==-2:
            msg.append("You have excessive Self Esteem and, belittles and manipulate others while Over-value yourself.")
        elif labelDict["Others Value"]==-1:
            msg.append("You have excessive Self Esteem and as a result don't value others opinion.")
        elif labelDict["Others Value"]==0:
            msg.append("You have excessive Self Esteem.")
        elif labelDict["Others Value"]==1:
            msg.append("You have excessive Self Esteem while also tend to value what someone has to say.")
    elif labelDict["Self Esteem"]==2:
        if labelDict["Others Value"]==-2:
            msg.append("You have high Self Esteem and, belittles and manipulate others.")
        elif labelDict["Others Value"]==-1:
            msg.append("You have high Self Esteem and don't value others opinion.")
        elif labelDict["Others Value"]==0:
            msg.append("You have high Self Esteem.")
        elif labelDict["Others Value"]==1:
            msg.append("You have high Self Esteem while also tend to value what someone has to say.")
    elif labelDict["Self Esteem"]==1:
        if labelDict["Others Value"]==-2:
            msg.append("You show a little Self Esteem but still belittles and manipulate others.")
        elif labelDict["Others Value"]==-1:
            msg.append("You have a little Self Esteem but also dosen't value others opinion.")
        elif labelDict["Others Value"]==0:
            msg.append("You show a little Self Esteem.")
        elif labelDict["Others Value"]==1:
            msg.append("You have a little Self Esteem and value what someone has to say, their opinian.")
    elif labelDict["Self Esteem"]==0:
        if labelDict["Others Value"]==-2:
            msg.append("You belittle others and try to manipulate them, making them do what you want.")
        elif labelDict["Others Value"]==-1:
            msg.append("you don't value others opinion and tend to impose them with your thoughts.")
        elif labelDict["Others Value"]==0:
            msg.append("You show a little to no Self Esteem.")
        elif labelDict["Others Value"]==1:
            msg.append("You posses a Helping nature and Value people around you.")
    
    # for observant
    if labelDict["Observant"]==2:
        msg.append("You are very Observant of your surrounding and focus on Details.")
    elif labelDict["Observant"]==1:
        msg.append("You are Detail oriented and have a keen eye on things happening around you.")
    elif labelDict["Observant"]==0:
        msg.append("You are not much as an Observent person but only selectively focus on things.")
    elif labelDict["Observant"]==-1:
        msg.append("You don't give attention to details instead look on the wider perspective.")

    # for vision
    if labelDict["Vision"]==1:
        msg.append("You have a Global vision and can't work in a Routine.")
    elif labelDict["Vision"]==-1:
        msg.append("You tend to live in present and complete tasks in front of you, usually following a Routine.")
    """elif labelDict["Vision"]==0:
        msg.append("You don't have Global vision.")"""
    
    # for self confidence
    if labelDict["Self Confidence"]==2:
        msg.append("You are highly Confident and sometimes even Over-confident.")
    elif labelDict["Self Confidence"]==1:
        msg.append("You are Confident and believe in yourself.")
    elif labelDict["Self Confidence"]==0:
        msg.append("You are Confident in doing things you know while usually neutral.")
    elif labelDict["Self Confidence"]==-1:
        msg.append("You lack Self-confidence.")
    
    # for extrovert and introver
    if labelDict["Extrovert"]==labelDict["Introvert"] and labelDict["Introvert"]!=0:
        msg.append("You can be Extrovert or Introvert depending on your company, we can say that there is a balance in your behaviour.")
    elif labelDict["Extrovert"]==0 and labelDict["Introvert"]==0:
        msg.append("You are neither Extrovert nor Introvert, simply neutral around people.")
    elif labelDict["Introvert"]==0:
        if labelDict["Extrovert"] in (3,4):
            msg.append("You are highly Extrovert and open up easily.")
        elif labelDict["Extrovert"]==2:
            msg.append("You are quite Extrovert and like to be around people.")
        elif labelDict["Extrovert"]==1:
            msg.append("You have an Extroverts personality.")
    elif labelDict["Introvert"] in (1,2):
        if labelDict["Extrovert"] in (3,4):
            msg.append("You are mostly Extrovert but also are selectively Introvert to some people.")
        elif labelDict["Extrovert"] in (1,2):
            msg.append("You can be Extrovert or Introvert depending on your company, we can say that there is a balance in your behaviour.")
        elif labelDict["Extrovert"]==0:
            msg.append("You have an Introverts personality.")
    elif labelDict["Introvert"] in (3,4):
        if labelDict["Extrovert"] in (3,4):
            msg.append("You can be Extrovert or Introvert depending on your company, we can say that there is a balance in your behaviour.")
        elif labelDict["Extrovert"] in (1,2):
            msg.append("You are usually Introvert but can be Extrovert if around people you are comfortable with.")
        elif labelDict["Extrovert"]==0:
            msg.append("You are highly Introvert and try to avoid people.")
    elif labelDict["Introvert"]==5:
        if labelDict["Extrovert"] in (3,4):
            msg.append("You are highly Introvert but still don't deny people for your company.")
        elif labelDict["Extrovert"] in (2,1):
            msg.append("You are highly Introvert and try to avoid people.")
        elif labelDict["Extrovert"]==0:
            msg.append("You are highly Introvert and wish to be left alone.")
        
    # for generous
    if labelDict["Generous"]==3:
        msg.append("You have a Helping nature and are generous to people around you.")
    elif labelDict["Generous"]==2:
        msg.append("You try to help people around you and are kind to them.")
    elif labelDict["Generous"]==1:
        msg.append("You are Kind and Generous to everyone.")
    elif labelDict["Generous"]==0:
        msg.append("You are not quite Generous but still have a Helping nature.")
    elif labelDict["Generous"]==-1:
        msg.append("You have a critics personality and people mistakes it for you being less Generous.")

    # for Selfish
    if labelDict["Selfish"]==1:
        msg.append("You are selfish and self-centered.")
    """elif labelDict["Selfish"]==0:
        msg.append("You are not selfish.")"""

    # for polite
    if labelDict["Polite"] in (-4,-3):
        msg.append("You are a very Arrogant person.")
    elif labelDict["Polite"] in (-2,-1):
        msg.append("You are Impolite to people under you.")
    elif labelDict["Polite"]==0:
        msg.append("You are neither too Polite nor too Impolite, just knows where to be Polite and where not to be.")
    elif labelDict["Polite"]==1:
        msg.append("You are Polite to people around you.")
    elif labelDict["Polite"]==2:
        msg.append("You have Good manners and are very Polite.")
    
    # for management
    if labelDict["Management"]==1:
        msg.append("You have good Managerial qualities.")
    elif labelDict["Management"]==-1:
        msg.append("You are bad at managing tasks.")
    """elif labelDict["Mnagement"]==0:
        msg.append("You don't have Global vision.")"""

    # for honesty
    if labelDict["Honesty"]==2:
        msg.append("You are very Honest and do your task Truthfully.")
    elif labelDict["Honesty"]==1:
        msg.append("You are an Honest person.")
    elif labelDict["Honesty"]==-1:
        msg.append("You are not Honest to yourself and Lie to get out of difficult situations.")
    """elif labelDict["Honesty"]==0:
        msg.append("You are neither too Polite nor too Impolite, just knows where to be Polite and where not to be.")"""
    
    # for emotional
    if labelDict["Emotional"]==2:
        msg.append("You are Emotionally stable and don't show your feelings easily.")
    elif labelDict["Emotional"]==1:
        msg.append("You get Emotional but knows how to control your emotions.")
    elif labelDict["Emotional"]==0:
        msg.append("You are a little sensitive.")
    elif labelDict["Emotional"]==-1:
        msg.append("You show emotions quite easily.")

    # for practical
    if labelDict["Practical"]==2:
        msg.append("You are Practical and tend to see things more on logical basis than just emotionally.")
    elif labelDict["Practical"]==1:
        msg.append("Your approach is always Practical and are good at Decision making.")
    elif labelDict["Practical"]==0:
        msg.append("You think both logically and emotionally.")
    elif labelDict["Practical"]==-1:
        msg.append("You are not good at Decision making.")
    elif labelDict["Practical"]==-2:
        msg.append("You are very bad in taking Decisions.")
    
    # for adjustment
    if labelDict["Adjustment"]==2:
        msg.append("You easily Adjust to your surrounding and become one with any company you have.")
    elif labelDict["Adjustment"]==1:
        msg.append("Your tend to Adjust yourself accoding to the people you are around.")
    elif labelDict["Adjustment"]==-1:
        msg.append("You have difficulty in Adjusting in some situations.")
    elif labelDict["Adjustment"] in (-2,-3):
        msg.append("You are bad in Adjusting to your surrounding and thus become uncomfortable easily.")
    """elif labelDict["Adjustment"]==0:
        msg.append("You think both logically and emotionally.")"""

    # for concentration
    if labelDict["Concentration"] in (3,2):
        msg.append("You have a very high Concentration.")
    elif labelDict["Concentration"]==1:
        msg.append("You Concentrate to a single task at a time.")
    elif labelDict["Concentration"]==-1:
        msg.append("You lack concentration and are easily diverted by disturbances.")
    """elif labelDict["Concentration"]==0:
        msg.append("You think both logically and emotionally.")"""
    
    # for imagination
    if labelDict["Imagination"]==2:
        msg.append("You have a very good Memory and Imagination power.")
    elif labelDict["Imagination"]==1:
        msg.append("Your Imagination can literally take you to worlds :P.")
    elif labelDict["Imagination"]==-1:
        msg.append("You are bad at imaginating scenarios and keeps forgetting things.")
    """elif labelDict["Imagination"]==0:
        msg.append("You think both logically and emotionally.")"""

    # for conservative
    if labelDict["Conservative"]==2:
        msg.append("You have Conserrvative nature and are Traditional.")
    elif labelDict["Conservative"]==1:
        msg.append("Your ideology is Conservative and you hold onto that.")
    elif labelDict["Conservative"]==0:
        msg.append("You are not Conservative.")
    
    # for dependent
    if labelDict["Dependent"]==2:
        msg.append("You are highly Dependent on others and need people around you at all the times.")
    elif labelDict["Dependent"]==1:
        msg.append("You Depend on others for comforting you.")
    elif labelDict["Dependent"]==0:
        msg.append("You only require people for comforting at your lowest.")
    elif labelDict["Dependent"] in (-1,-2):
        msg.append("You don't depend on others rather are a Lone-wolf.")

    # for self control
    if labelDict["Self Control"] in (3,2,1):
        msg.append("You have a high Self-Control and does not loose balance in chalanging situations.")
    elif labelDict["Self Control"]==0:
        msg.append("You posses Self-control but still tend to loose control in some situations.")
    elif labelDict["Self Control"]==-1:
        msg.append("You lack Self-control and become impulsive easily.")

    # for trust
    if labelDict["Trust"] in (2,1):
        msg.append("You Have Excessive trust on people.")
    elif labelDict["Trust"]==0:
        msg.append("You Trust people easily.")
    elif labelDict["Trust"]==-1:
        msg.append("You don't Trust people easily.")
    elif labelDict["Trust"]==-2:
        msg.append("You choose not to Trust anyone.")
    
    # for talkative
    if labelDict["Talkative"]==1:
        msg.append("You are a very Talkative Person.")
    elif labelDict["Talkative"]==0:
        msg.append("You only speak when necessary.")
    elif labelDict["Talkative"]==-1:
        msg.append("You are shy and don't speak untill forced to.")

    # for relate
    elif labelDict["Relate"]==-1:
        msg.append("You have difficulty to relate to what others are thinking.")

    # for stable
    if labelDict["Stable"]==1:
        msg.append("You are a Stable and calm Person.")
    elif labelDict["Stable"]==-1:
        msg.append("You become unstable quite easily and loose your calm.")

    # for expressive
    if labelDict["Expressive"]==0:
        msg.append("You can exress your thoughts easily.")
    elif labelDict["Expressive"]==-1:
        msg.append("You are unable to express what you feel and think to others.")

    # for perfectionist
    if labelDict["Perfectionist"]==2:
        msg.append("You like things to be perfect and are a Perfectionist.")
    elif labelDict["Perfectionist"]==1:
        msg.append("You do your job with utmost perfection.")
    elif labelDict["Perfectionist"]==-1:
        msg.append("Jobs you do are not done perfectly and tend to leave things on the flow.")

    # for initiation
    if labelDict["Initiation"]==2:
        msg.append("You are an expressive person and ready to Initiate tasks and even chatter.")
    elif labelDict["Initiation"]==1:
        msg.append("You would always Initiate the talk if gets a chance.")

    # for listner
    if labelDict["Listner"]==1:
        msg.append("You are a good Listener and try to understand what other has to say.")
    elif labelDict["Listner"]==0 and labelDict["Talkative"]==1:
        msg.append("You don't listen to others but always want them to listen to you.")

    for x in msg:
        print("->",x)