from flask import Flask, render_template
import os

# Production configuration for security
app = Flask(__name__, static_folder='static')

# Security settings for production
app.config['DEBUG'] = False  # Disable debug mode in production
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'furore-2026-production-key') if not app.debug else 'dev-key'

# Add pictures folder as additional static directory
app.static_folder = 'static'

# FURORE 2026 - Dayananda Sagar College of Engineering Cultural Fest
# Website developed by Arya Sharan (aryasharan@example.com)
# Backend development, frontend design, and deployment integration

SCORING_LEGEND = {5: 500, 4: 400, 3: 300, 2: 200, 1: 100}


def event(name, stars, description, registration_fee, prize_pool, contacts, rules):
    return {
        "name": name,
        "stars": stars,
        "description": description,
        "registration_fee": registration_fee,
        "prize_pool": prize_pool,
        "contacts": contacts,
        "rules": rules,
    }


CLUSTERS = {
    "sovereign-stage": {
        "name": "The Sovereign Stage",
        "icon": "🎭",
        "weightage": "35%",
        "description": "Cluster 1: Stage arts, dance, and live performance.",
        "events": [
            event("The Battle of Silhouettes (Fashion Show)", 5, "A fashion showcase inspired by strength, structure, and bold expression under an open theme.", "INR 3,000", "Prize Pool: INR 40,000", "Disha Kabra (8441878592), Athreya Upadhyaya (7892876965)", "Groups of 8-10 must perform for 6-8 minutes. Outfits must be modest. Wearing heels is compulsory; failure to do so leads to negative marking."),
            event("Royal Rhythm (Group Dance)", 5, "A group dance competition featuring Western or Eastern (classical, semi-classical, folk) categories.", "INR 1,000", "If there are less than 5 teams only first prize will be awarded", "Kanan (9108089514), Manikya (8861433696)", "Teams of 5-15 members. Duration is 5+1 minutes. Audio track to be submitted 3 days before the event."),
            event("Battle Of Bands", 5, "Open music competition for college, professional, and semi-professional bands.", "INR 1,500", "Winners: INR 15,000; Runners Up: INR 10,000", "Shashank (8904284586), Harsh (9599001759)", "Teams of 5-10 members. Time limit is 10+5 minutes including sound check. Original compositions hold higher weightage. No backing tracks or synthesized beats."),
            event("Street Play", 5, "Dramatics competition performed in open areas using any theme.", "INR 599", "Winners: INR 6,000; Runner Ups: INR 3,000", "Likith Vignesh (9380942252), Inaya Kazi (88849 56030)", "Teams of 8-15 members. Performance time limit is 10+5 minutes. Performances can be in Kannada, Hindi, or English."),
            event("Mime", 4, "A theatrical performance cluster focusing on silent expression through movement.", "INR 499", "Winners: INR 4,000; Runner Ups: INR 2,000", "Lhohannkumaarr (9731297485), Sujay Naganur (6364911458)", "Teams of 6-10 members. Performance time is 8-10 minutes. Background music is allowed, but no props are permitted."),
            event("Battle Of The Crown (Dance Battle)", 4, "Individual all-style 1v1 dance battle.", "INR 500", "Not specified", "Manvith (7892296607), Abhishek (7009032844)", "Round 1 is 1 minute; Round 2 duration is determined by judges. Music is provided on the spot. On-the-spot registration is available."),
            event("Crown Taker (Western Solo Dance)", 3, "Individual Western dance performance competition.", "INR 300", "Winner: INR 3,000", "Sinchana (9148328778), Om (9019328304)", "Time limit is 3+1 minute. Audio must be submitted in the specified format before the event. Green rooms are provided."),
            event("Eastern Solo Dance", 3, "Individual performance of traditional classical or folk dance styles.", "INR 350", "Prize Pool: INR 4,000", "Dhanya Jogbhat (9535355394), Harini P (9148818022)", "Time limit is 4+1 minute. No props that dirty the stage or inflammable materials. Report 30 minutes prior to the event."),
            event("Eastern Vocals", 3, "Solo singing competition for songs in any Indian language.", "INR 250", "Winners: INR 2,500; Runners Up: INR 1,500", "Gayan (9591995566), Kavana (7829977032)", "Time limit 3+2 minutes. One accompanist or backing track/Tanpura allowed. No lyrics reference allowed while singing."),
            event("Western Vocals", 3, "Solo singing competition for English songs.", "INR 250", "Winners: INR 2,500; Runners Up: INR 1,500", "Sammita (9535729696), Ezra (6390055985)", "Time limit 3+2 minutes. Participants cannot refer to lyrics while singing. Backing track or one accompanist allowed."),
            event("Instrumental Solo", 3, "Solo musical performance using any instrument.", "INR 250", "Winners: INR 2,500; Runners Up: INR 1,500", "Bala Murali (6383546926), Deepanjan (7004035118)", "Time limit is 3+2 minutes including setup. Participants must bring their own instruments. One accompanist is allowed to play an instrument only."),
            event("Rap", 2, "Three-round competition: Showcase (2+1 mins), Freestyle (1 min), and Battle round (16 bars).", "INR 250", "Winners: INR 2,000", "Snehal (9749798087), Shuvam (8583054679)", "No language barriers. Original compositions are entertained. Backing track for showcase must be submitted 2 days prior."),
            event("Beatbox", 2, "Three-round tournament judged on flow, originality, and clarity.", "INR 250", "Winners: INR 2,000", "Adhish (9111967315), Saishree (9972300967)", "Includes a showcase (2 mins) and 1v1 battles (60/90 sec). Backing tracks are strictly not allowed."),
        ],
    },
    "artisans-guild": {
        "name": "The Artisan's Guild",
        "icon": "🛡️",
        "weightage": "20%",
        "description": "Cluster 2: Creativity and visual content.",
        "events": [
            event("Crown Cuts (Reel Making)", 4, "Content creation competition involving format-specific evaluation rounds.", "INR 250", "Winners: INR 1,500; Runners Up: INR 800", "Adarsh (9611802661), Mohan (9641026036)", "Participants must report on time for offline rounds. No plagiarism or external assistance. Mobile devices may be restricted during specific rounds."),
            event("Lense Of Legends (Photography)", 3, "Individual on-the-spot photography event within college grounds.", "INR 250", "Winner: INR 2,000; Runner Up: INR 1,000", "AbhiRam (6281201364), Shubha (8402025755)", "4-hour time limit. Minimal editing and color correction allowed; manipulation or plagiarism leads to disqualification. Only one image can be submitted."),
            event("Elemental Roulette (Painting)", 3, "Individual 2-hour painting challenge themed around 4 selected 'Kingdom Elements'.", "INR 200", "Winner: INR 2,000; Runner: INR 1,000", "Soujanya (8660557754), Utpala (9591655482)", "Participants must bring their own paints and materials. No phones, reference images, or external assistants. Elements cannot be swapped once chosen."),
            event("Clueminati", 2, "Narrative-driven event where participants decipher 10 clues to advance a story.", "Individual: INR 75; Team of 2: INR 150", "Winners: INR 1,500; Runners: INR 1,000", "Srishti Krishna Hegde (9845275156), Eesha Hemani (9686714422)", "Individual or teams of 2. No internet or cheating. Max 3 hints allowed per group with point deductions."),
            event("Tattoo Design", 1, "Individual competition focused on creating original tattoo designs on provided templates.", "INR 200", "Winners: INR 2,000; Runners: INR 1,000", "Chandrima (7044468839), Nishanth (8217871629), Bhuvan (8431530319)", "Design must be original and made only during competition time. Copied or traced designs are not allowed. No offensive or vulgar content."),
            event("Witcraft", 1, "Three-round literary competition: Genre Fusion, Literary Buzz, and a Surprise Round.", "INR 75", "Winners: INR 1,000; Runners: INR 500", "Naisha (9606484338), Sneha (8318900805)", "Individual event. Internet use or plagiarism is strictly prohibited. Participants are judged on creativity, originality, and wit."),
        ],
    },
    "kings-council": {
        "name": "The King's Council",
        "icon": "📜",
        "weightage": "15%",
        "description": "Cluster 3: Debate, literary, quiz, and management events.",
        "events": [
            event("DiploMaze (MUN)", 5, "Fast-paced Mini Model United Nations simulation focused on high-pressure diplomacy.", "Not specified", "Cash Prize Pool: INR 6,000 (Best Delegate 3000; High Commendation 2000; Special Mention 1000)", "Anish G (8073459615)", "4-5 hour timeframe. Delegates represent countries to resolve a global agenda through negotiations. Includes informal lobbying and twists."),
            event("Warriors Of The Mind (Quiz)", 3, "General knowledge quiz consisting of rounds of questions and trivia.", "INR 250", "Prize Pool: INR 5,500 (1st prize 3500; 2nd prize 2000)", "Saadyant PR (9353459644), Aditya Kahali (9301806057)", "Team size 1-3 members. Electronic items are strictly prohibited. Quizmaster has the final say."),
            event("The Final Decree (Debate)", 4, "Individual debate competition where arguments 'shape the fate of empires'.", "INR 250", "Prize Pool: INR 6,000 (1st prize 4000; 2nd prize 2000)", "Micah (6364553991)", "Topics given on the spot with prep time. Round 1 is 1v1 debate. Use of AI tools is discouraged."),
            event("Rise To Reign (The Best Manager)", 4, "Management event testing business awareness and crisis management through 4 competitive rounds.", "INR 200", "Prize Pool: INR 6,000", "Arshi Anirudh (9148290373), Ishaan Saxena (7490004027)", "Participants must register by the deadline. Case study must be submitted pre-event. Carrying valid college ID is mandatory for offline rounds."),
            event("War Of Wits", 3, "A 2-day individual challenge testing spontaneous thinking and creativity over 3 rounds.", "INR 150", "Winners: INR 2,500; Runners Up: INR 1,500", "Aarya (7303447817), Naman (8334072002)", "English is the only language permitted. Must qualify preliminary rounds to be a finalist. No vulgarity or controversial political topics."),
            event("Tick Tock Your Majesty (Just-A-Minute)", 2, "Classic JAM session testing eloquence, sharpness, and command over speech.", "INR 100", "Prize Pool: INR 5,000 (1st prize 3000; 2nd prize 2000)", "Rohith B N (8618294710), Ujjwal Moolchandani (8792859708)", "Standard JAM rules apply. Bonus points for wit and humor. One careless 'umm' or misplaced word can lose the round."),
            event("The Royal Wordfest", 3, "Individual competition featuring 'Spin the Yarn' (on-the-spot storytelling) and 'Turncoat' (stance-switching debate).", "INR 150", "Prize pool 3000 (1st prize 2000; 2nd prize 1000)", "Nimai (6363129609), Ujjwal (8792859708), Micah (6364553991)", "For Round 1, topic changes every minute for 3 minutes. For Round 2, you must switch stance on the judge's signal. 2-minute total speaking time for Turncoat."),
            event("Throne Of Jokes (Stand-Up Comedy)", 2, "A two-stage battle of comedy where 'humour is your weapon'.", "INR 150", "Winners: INR 2,000; Runners Up: INR 1,000", "Nidhi (8317311680), Ashlesh (9113013196)", "Individual sets of 2-3 minutes. Languages: English, Hindi, or Kannada. Must be original content; no plagiarism."),
            event("Abhivyakti (Hindi Poetry)", 1, "Two-round Hindi self-composed poetry competition.", "INR 200", "Prize Pool: INR 4,000 (1st prize 2500; 2nd prize 1500)", "Soumya Gauraha (7024299361), Devansh Sharma (9380548103), Yash Raj (8319593584)", "Individual event. Round 1 theme given 1 day prior. Presentation time is 3-4 minutes. Mobile phones and notes are prohibited on stage."),
            event("Sceptre Et Slam (Slam Poetry)", 1, "Poetry writing and performance event for 'bards and troubadours'.", "INR 200", "Prize Pool: INR 8,000 (1st prize 5000; 2nd prize 3000)", "Aditya Dushad (7905091467), Nimai RS (6363129609)", "45 minutes to write on a displayed theme. Poetry format only. 2-minute presentation limit. No electronics, costumes, or music."),
            event("Yuddhakaanda (Kannada Literature)", 1, "Three-round journey through film and history: Quiz, Mystery round, and Debate.", "INR 100", "Prize Pool: INR 4,000 (1st prize 2500; 2nd prize 1500)", "Spandana RN (7899295054), Sinchana HP (7483658217)", "Team size of 2 members. General rules involve quick thinking and eloquence in Kannada."),
        ],
    },
    "warriors-arena": {
        "name": "Warriors Arena",
        "icon": "⚔️",
        "weightage": "30%",
        "description": "Cluster 4: Arena games, esports, and tactical team events.",
        "events": [
            event("Damsel In Distress (Rescue The Lost Princess)", 1, "Campus-wide rescue mission where 'kidnappers' in black roam to tag teams.", "INR 300 per team", "First Prize: 1000; Runner-Up: 500", "Animesh (7898623683), Thanmitha (8050537588)", "Teams of 4-5 members with at least one female participant. Each team must carry a flag visibly. Getting caught adds 2 minutes to total time."),
            event("Jugaad Tank (Yen Idea Guru)", 2, "Satirical pitch competition selling 'sasta' products through audacity and fake stats.", "INR 150 per Team", "Winners: INR 2,000; Runners Up: INR 1,000", "Arya (9110648489), Jaanvi (9777169203)", "Teams pick one random product; 60 seconds to prep and 120 seconds to pitch. Both partners must participate. Ridiculous equity asks are mandatory."),
            event("Goal Of Thrones (7v7 Football)", 3, "Seven-a-side football tournament testing skill and speed on the field.", "INR 1000", "Winners: INR 6,000; Runners Up: INR 3,000", "Ayman (6364308887), Rayaan (7259903344)", "Team of 7 players on field with up to 2 substitutes. Match duration is 20-30 minutes. Draws lead to penalty shootouts. Ref decision is final."),
            event("Squid Game", 4, "Multi-round strategic and physical elimination games where only one winner remains.", "INR 400 per team", "Winners: INR 4,000; Runners Up: INR 2,000", "Maheswar (9110362205), Anish (8197081650)", "Teams of exactly 4 members with no substitutions. Comfortable clothes suitable for physical activity are required. Misbehavior results in instant removal."),
            event("BGMI", 4, "Mobile esports tournament focused on TDM knockout rounds.", "FREE", "Prize Pool: INR 10,000", "Anirudh Sondur (8104631569)", "Squad entry (4 members) with valid BGMI IDs. Mobile devices only (no emulators/tablets/triggers). Matches will not be restarted for latecomers."),
            event("Mock IPL Auction", 4, "Strategic two-round bidding event (Quiz followed by Auction) using a 100-crore budget.", "INR 200 per team", "Winners: INR 3,000; Runners Up: INR 1,500", "Shreya (9353321622), Preetham (7259247858)", "Teams of 12-14 players with specific role requirements (e.g., 3-4 Bowlers, 1 Wicketkeeper). 3-5 foreign players allowed per squad. Bid increments vary based on current price."),
            event("Treasure Hunt", 3, "Campus-wide competition solving clues to retrieve items.", "INR 400 per team", "Winners: INR 9,000; Runners Up: INR 3,000", "Chethan (8904694138), Sajidha (7619525123)", "Team of 4 members. Teams must stay together at all times. Phones with internet access are encouraged. Destroying clues leads to disqualification."),
        ],
    },
}


def add_computed_fields(clusters):
    for cluster_id, cluster in clusters.items():
        events = sorted(cluster["events"], key=lambda item: item["stars"], reverse=True)
        cluster["events"] = events
        cluster["id"] = cluster_id
        cluster["event_count"] = len(events)
        cluster["max_points"] = sum(SCORING_LEGEND[event["stars"]] for event in events)
        for event in events:
            event["first_points"] = SCORING_LEGEND[event["stars"]]
            event["second_points"] = SCORING_LEGEND[event["stars"]] // 2
            event["stars_emoji"] = "★" * event["stars"]
            event["register_link"] = "/register-info"
    return clusters


CLUSTERS = add_computed_fields(CLUSTERS)


@app.route("/")
def home():
    return render_template("index.html", clusters=CLUSTERS)


@app.route("/events")
def events():
    return render_template("events.html", clusters=CLUSTERS)


@app.route("/about")
def about():
    return render_template("about.html", clusters=CLUSTERS, scoring_legend=SCORING_LEGEND)


@app.route("/guidelines")
def guidelines():
    return render_template("guidelines.html")


@app.route("/register-info")
def register_info():
    return render_template("register_info.html")


@app.route("/brochure")
def brochure():
    return render_template("brochure.html")


if __name__ == "__main__":
    app.run(debug=True)
