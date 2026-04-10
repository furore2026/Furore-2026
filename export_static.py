#!/usr/bin/env python3
"""
Static Export Script for Netlify Deployment
Exports Flask app as static HTML files
"""

from flask import Flask, render_template
import os
import shutil

app = Flask(__name__)

# Load your clusters data (same as in app.py)
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
            event("Fashion", 5, "Open-theme fashion showcase judged on choreography, creativity, and props.", "INR 3,000", "Prize Pool: INR 40,000", "Disha Kabra (8441878592), Athreya Upadhyaya (7892876965)", "Team 8-10; 6+2 mins; no hazardous equipment."),
            event("Group Dance", 5, "Group dance event in Western or Eastern categories.", "Not specified", "Not specified", "Kanan (9108089514), Manikya (8861433696)", "Team 5-15; 5+1 mins; audio in advance."),
            event("Battle Of Bands", 5, "Open for college, professional, and semi-professional bands.", "INR 1,500", "Winner: INR 15,000 | Runner Up: INR 10,000", "Shashank (8904284586), Harsh (9599001759)", "Team size 5-10; no backing tracks."),
            event("Street Play", 5, "Outdoor drama performance with open themes.", "INR 599", "1st: INR 6,000 | 2nd: INR 3,000", "Likith Vignesh (9380942252), Inaya Kazi (8884956030)", "Team 8-15; 10+5 mins; props allowed."),
            event("Mime", 4, "Silent performance act judged on expression and storytelling.", "Not specified", "Not specified", "To be announced", "No spoken dialogue during performance."),
            event("Dance Battle", 4, "On-the-spot individual dance battle with music by organizers.", "INR 500", "Prize Pool: INR 6,000", "Manvith (7892296607), Abhishek (7009032844)", "Two rounds; open category."),
            event("Western Solo Dance", 3, "Individual western dance performance.", "INR 300", "Winner: INR 3,000", "Sinchana (9148328778), Om (9019328304)", "3+1 mins."),
            event("Eastern Solo Dance", 3, "Individual performance in Indian classical or folk forms.", "INR 350", "Prize Pool: INR 4,000", "Dhanya Jogbhat (9535355394), Harini P (9148818022)", "4+1 mins."),
            event("Eastern Solo Singing", 3, "Vocal competition for songs in any Indian language.", "INR 250", "Winner: INR 2,500 | Runner Up: INR 1,500", "Gayan (9591995566), Kavana (7829977032)", "3+2 mins."),
            event("Western Solo Singing", 3, "English vocals competition.", "INR 250", "Winner: INR 2,500 | Runner Up: INR 1,500", "Sammita (9535729696), Ezra (6390055985)", "3+2 mins."),
            event("Instrumental Solo", 3, "Individual instrumental performance challenge.", "INR 250", "Winner: INR 2,500 | Runner Up: INR 1,500", "Bala Murali (6383546926), Deepanjan (7004035118)", "Bring own instrument."),
            event("Rap", 2, "Three-round format with showcase, freestyle, and battle round.", "INR 250", "Winner: INR 2,000", "Snehal (9749798087), Shuvam (8583054679)", "Originals encouraged; submit showcase track 2 days prior."),
            event("Beatbox", 2, "Showcase and battle-format beatbox tournament.", "INR 250", "Winner: INR 2,000", "Adhish (9111967315), Saishree (9972300967)", "Judged on flow/originality/clarity; no backing tracks."),
        ],
    },
    "artisans-guild": {
        "name": "The Artisan's Guild",
        "icon": "🛡️",
        "weightage": "20%",
        "description": "Cluster 2: Creativity and visual content.",
        "events": [
            event("Reel Making", 4, "Creation of short-form video content.", "INR 250", "Winner: INR 1,500 | Runner Up: INR 800", "Adarsh (9611802661), Mohan (9641026036)", "Follow format and time limits."),
            event("Photography", 3, "On-the-spot campus photography challenge.", "INR 250", "Winner: INR 2,000 | Runner Up: INR 1,000", "Abhiram (6281201364), Shubha (8402025755)", "4-hour limit; one image submission."),
            event("Elemental Roulette", 3, "Two-hour painting challenge themed on kingdom elements.", "INR 200", "Winner: INR 2,000 | Runner Up: INR 1,000", "Soujanya (8660557754), Utpala (9591655482)", "Bring own materials; no references."),
            event("Clueminati", 2, "Narrative clue-solving event for individuals or pairs.", "INR 75 (solo) | INR 150 (duo)", "Winner: INR 1,500 | Runner Up: INR 1,000", "Srishti Krishna Hegde (9845275156), Eesha (8686714422)", "No internet; max 3 hints."),
            event("Tattoo", 1, "Thematic tattoo design challenge.", "Not specified", "Not specified", "To be announced", "Original artwork only."),
            event("Witcraft", 1, "Creative quick-thinking and concept-building challenge.", "Not specified", "Not specified", "To be announced", "Judged on originality and presentation."),
        ],
    },
    "kings-council": {
        "name": "The King's Council",
        "icon": "📜",
        "weightage": "15%",
        "description": "Cluster 3: Debate, literary, quiz, and management events.",
        "events": [
            event("MUN", 5, "Mini Model United Nations simulation.", "Not specified", "Prize Pool: INR 6,000", "Anish G (8073459615)", "Committee protocol and diplomatic decorum."),
            event("Quiz", 3, "General knowledge and trivia competition.", "INR 180", "1st: INR 3,000 | 2nd: INR 2,000", "Saadyant PR (9353459644), Aditya Kahali (9301806057)", "Team size 1-3; no electronic items."),
            event("Debate", 4, "Two-round debate competition with 1v1 opener.", "INR 250", "1st: INR 4,000 | 2nd: INR 2,000", "Micah (6364553991)", "Topics announced on the spot."),
            event("Best Manager", 4, "Management event with quiz, GD, and crisis management rounds.", "INR 200", "Prize Pool: INR 6,000", "Arshi Anirudh (9148290373), Ishaan Saxena (7490004027)", "Carry valid ID; maintain professionalism."),
            event("War of Wits", 3, "2-day emcee/personality event testing creativity and spontaneity.", "INR 150", "Winner: INR 2,500 | Runner Up: INR 1,500", "Aarya (7303447817), Naman (8334072002)", "English only."),
            event("JAM", 2, "Just-A-Minute speaking event.", "INR 100", "1st: INR 5,000 | 2nd: INR 3,000", "Ujjwal Moolchandani (8792859708)", "No pauses or fillers."),
            event("Turncoat", 3, "Stance-switching debate format from subsoc combined event.", "INR 150", "Included in Royal Wordfest prizes", "Nimai (6363129609), Ujjwal (8792859708), Micah (6364553991)", "Rapid argument reversal round."),
            event("Standup", 2, "Stand-up comedy with qualifiers and final battle.", "INR 150", "Winner: INR 2,000 | Runner Up: INR 1,000", "Nidhi (8317311680), Ashlesh (9113013196)", "Original content only."),
            event("Hindi Poetry", 1, "Self-written Hindi poetry event.", "INR 200", "1st: INR 2,500 | 2nd: INR 1,500", "Soumya Gauraha (7024299361), Devansh Sharma (9380548103), Yash Raj (8319593584)", "3-4 min presentation."),
            event("English Poetry", 1, "Slam poetry writing and presentation event.", "INR 200", "1st: INR 5,000 | 2nd: INR 3,000", "Aditya Dushad (7905091467), Nimai RS (6363129609)", "Poetry-only format."),
            event("Kannada Poetry", 1, "Kannada literary event with quiz, mystery, and debate rounds.", "INR 100", "Prize Pool: INR 5,000", "Spandana RN (7899295054), Sinchana HP (7483658217)", "Team size: 2."),
        ],
    },
    "warriors-arena": {
        "name": "Warriors Arena",
        "icon": "⚔️",
        "weightage": "30%",
        "description": "Cluster 4: Arena games, esports, and tactical team events.",
        "events": [
            event("Damsel Distress", 1, "Campus-wide rescue challenge with roamers and timed penalties.", "INR 300 per team", "1st: INR 1,000 | Runner Up: INR 500", "Animesh (7898623683), Thanmitha (8050537588)", "Team 4-5; include at least one female participant."),
            event("Jugad Tank", 2, "Innovation challenge focused on practical solutions and pitching.", "Not specified", "Not specified", "To be announced", "Rapid prototyping with judged presentations."),
            event("Futsal", 3, "High-intensity team futsal competition.", "Not specified", "Not specified", "To be announced", "Team sport rules apply."),
            event("Squid Game", 4, "Team-based physical and strategic elimination challenge.", "INR 400 per team", "Winner: INR 4,000 | Runner Up: INR 2,000", "Maheswar (9110362205), Anish (8197081650)", "Team of 4; no substitutions."),
            event("BGMI", 4, "Mobile esports challenge with TDM knockout rounds.", "FREE", "Prize Pool: INR 10,000", "Anirudh Sondur (8104631569)", "Squad of 4; no emulators/tablets."),
            event("Mock IPL", 4, "Quiz plus auction simulation with 100-crore budget.", "INR 200 per team", "Winner: INR 3,000 | Runner Up: INR 1,500", "Shreya (9353321622), Preetham (7259247858)", "Team composition constraints apply."),
            event("Treasure Hunt", 3, "Campus clue race and retrieval event.", "INR 400 per team", "Winner: INR 19,000 | Runner Up: INR 3,000", "Chethan (8904694138), Sajidha (7619525123)", "Team of 4; stay together."),
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

def export_static():
    """Export all Flask routes as static HTML files"""
    
    # Create output directory
    if os.path.exists('output'):
        shutil.rmtree('output')
    os.makedirs('output')
    
    # Copy static files
    if os.path.exists('static'):
        shutil.copytree('static', 'output/static', dirs_exist_ok=True)
    
    # Export all routes
    routes = [
        ('index.html', 'home', {'clusters': CLUSTERS}),
        ('events.html', 'events', {'clusters': CLUSTERS}),
        ('about.html', 'about', {'clusters': CLUSTERS, 'scoring_legend': SCORING_LEGEND}),
        ('guidelines.html', 'guidelines', {}),
        ('register-info.html', 'register_info', {}),
        ('brochure.html', 'brochure', {}),
    ]
    
    for template, route_name, context in routes:
        rendered = render_template(template, **context)
        with open(f'output/{template}', 'w', encoding='utf-8') as f:
            f.write(rendered)
        print(f'Exported: {template}')
    
    print(f'✅ Static site exported to output/ directory!')
    print(f'📁 Ready for Netlify deployment!')
    print(f'🌐 Upload the "output" folder to Netlify')

if __name__ == "__main__":
    export_static()
