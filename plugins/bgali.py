"""
plugin for ultroid by @moon_knight69 and @itzyournil and our sir @baba_riddle
✘ Commands Available
✘ bangla গালি  (bangla)

> CMD: `{i}gandu`
"""

from telethon import events
import random, re
from . import ultroid_cmd

RUNSREACTS = [
    "`মাসুদ ভালো হয়ে যাও `",

    "`বাল ফালায়া খালে নামাইয়া দিমু একদম`",
    
    "`কনডম চোর",

    "` তোমার ফুক্কি দিয়া রড ঢুকামু `",

    "বাল ফালায়া খালে নামাইয়া দিমু একদম `",

"` মানুষ চিনো , প্যান্ট এর ভিতর বরফ পানি ঢাইলা দিমু `",

"`আমারটা দেখলে খাড়ায় মুইতা দিবি বহনের টাইম পাবি না `",

"`তোর সানডে মানডে ক্লোজ কইরা দিমু `",

" `আয় চল পাট ক্ষেতে `যাই",

" `মাসুদ ভালো হয়ে যাও `",

"`লেওড়াদোচা`",


" `জাবি নাকি আবাসিকে `",

"`তোরে লইয়া আজকে একটা ফাটাফাটি হইবো`",

" মগার বাচ্ছা `",

"`Gua মারা খা`",

" `ইদুর খাইয়া নেশা করছস` ",

"` নসুর ঘরে নসু ",

    "`তোর ফুটকি হেলিকপ্টার ঢুকাবো `",

    "`তোর গারে ট্রেন ঢুকাবো`",

    "`জং ধরা লোহা দিয়া পাকিস্তানের মানচিত্র বানাই্য়া তোদের পিছন দিয়া ঢুকামু`",

    "`আহো ভাতিজা, আহো, দেখছো? তোমার লাইগা কত বড় ফুকনি ডা রাইখা দিছি, আর এইডা তোমার পা*া দিয়া ঢুকায়া দিমু 😂😂.`",
    
    "`ঐ বোকা*দা কয় কি !.`",
    "`হারামজাদা`",

    "'মাগিবাজ`",

    "মীরজাফর",

 "`ধোন কাইট্টা কুত্তা দিয়া খাওয়ামু`",

 "পুক্কি ফাতাফাতা কইরা হালামু খামকির ছেলে",


    "'তোর জাঙ্গীয়া খুইল্যা আগুন লাগায় দিমু`",

    "`মাকি না খোঁজে নিজের লুলি দিয়ে নিজের টুপকি মারো`",

    "`তুই তো শালা ফাটা বেলুনের ফসল`",

    "`বানচোত`",

    "`মোবাইল ভাইব্রেশন কইরা ভইরা দিবো`",

    "`আই হাই উস্তাদ কাম হইয়া গ্যাছে, গুয়া মারা সারা `",
    
    "`পুক্কি মারা খা`",
    
    "তুরি মেরে ভুঁড়ি ফাটিয়ে দিবো তোর " ,
    
" তোর মত ইদুর চো*দা খুব কম দেখছি",
" বিচি কাইটা হাতে ধরায় দিমু ",

" ২ ইঞ্চি লুলি দিয়ে ভালোবাসা পাবি না ",

" মাগী না চু*দে ৪০ টাকা দিয়ে ম্যাগী খা ",

" তোর ট্যাংকি ফুটা কইরা দিমু ",

" এই নাটকীর পু ",

" চুটকি বাজিয়ে ফুটকি মেরে দিবো ",

" গাধা দিয়ে বাসর রাত সম্ভব না ",

" গাধা কোথাকার",

" কিরে ঘর জামাই চো*দা ",

" নটি মাগী ",

" আবুল গিরি কম কর ",

" কিরে আবাল ",

" কিরে বোদায় চো*দা ",
]

@ultroid_cmd(pattern="gandu")
async def _(event):
    if event.fwd_from:
         return
    bro = random.randint(0, len(RUNSREACTS) - 1)    
    reply_text = RUNSREACTS[bro]
    await event.edit(reply_text)
