#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Content + page assembly for londonhvacpros.ca. Run: python3 build_pages.py"""
from build import *  # noqa

# ============================================================ SERVICE DETAILS
SVC = {
 "furnace-repair": {
   "icon":"flame", "kicker":"Furnace Installation &amp; Repair in London, Ontario",
   "h1":"High-Efficiency Furnace Installation and Repair",
   "intro":"Whether you are upgrading to a high-efficiency furnace or keeping your current one running well, London HVAC Pros has the install expertise to do it right. We serve London, Ontario and the surrounding Middlesex County communities, sizing each new furnace to the home it heats and installing it to manufacturer spec. The payoff is steadier warmth, lower gas bills, and a system that holds up through every Ontario winter.",
   "meta":"High-efficiency furnace installation & repair in London, Ontario. Right-sized systems, rebate guidance & expert service from licensed techs. Free quote.",
   "problem_h":"Furnace aging, costly to run, or due for an upgrade?",
   "problem_p":"London HVAC Pros installs and services high-efficiency furnaces in London, ON, sized to your home for lower bills and reliable heat.",
   "features":[
     ("flame","Right-Sized High-Efficiency Installs","We run a proper load calculation before recommending a furnace, so your new high-efficiency system matches your home instead of guessing. Correct sizing means even heat, quieter operation, and lower gas use."),
     ("settings","Tune-Ups That Protect Efficiency","A furnace loses efficiency without upkeep. We check airflow, filters, burners, and the heat exchanger to keep your system running at the rating it was installed to deliver, and to protect the warranty."),
     ("shield","Certified Installers, Clear Pricing","Our licensed technicians install and service every major furnace brand, including high-efficiency models, and explain the efficiency ratings and rebate options before any work begins."),
   ],
   "rev":[0,1,2],
 },
 "ac-repair": {
   "icon":"snowflake", "kicker":"AC Installation &amp; Repair in London, ON",
   "h1":"High-Efficiency AC Installation and Repair",
   "intro":"A new high-efficiency air conditioner cools your home on less power and runs quieter doing it. London HVAC Pros installs and services central air across London and the surrounding Middlesex County communities, matching each unit to the home it cools so it holds temperature without overworking. When an existing system needs attention, our technicians diagnose it accurately and get your comfort back fast.",
   "meta":"High-efficiency AC installation & repair in London, Ontario. Right-sized central air & ductless systems from licensed local techs. Free quotes.",
   "problem_h":"Old AC struggling, loud, or expensive to run?",
   "problem_p":"London HVAC Pros installs and services high-efficiency central air and ductless systems in London, ON, sized for quiet, low-cost cooling.",
   "features":[
     ("snowflake","Efficient Cooling, Properly Sized","We size your new air conditioner to your home rather than to the old unit, so it cools evenly, runs less, and keeps your summer energy bills in check. Higher SEER ratings mean real savings season after season."),
     ("settings","Seasonal Service That Keeps SEER High","An AC drifts off its rated efficiency without care. We check refrigerant, coils, airflow, and controls so your system delivers the cooling and economy it was built for."),
     ("shield","Certified Techs, Honest Quotes","Our licensed technicians install and service all major AC brands, walk you through efficiency ratings and rebate options, and give clear pricing before the work starts."),
   ],
   "rev":[3,4,5],
 },
 "ductless-ac-installation": {
   "icon":"fan", "kicker":"Ductless AC Installation in London, Ontario",
   "h1":"Energy-Efficient Ductless Mini-Split Installation",
   "intro":"Ductless mini-splits bring efficient heating and cooling to spaces a central system can't reach well: additions, finished basements, and older homes without ductwork. London HVAC Pros installs high-performance ductless systems across London, Ontario and the surrounding Middlesex County areas, planning the zoning around how you actually use each room. The result is quiet, room-by-room comfort and lower energy bills.",
   "meta":"Professional ductless mini-split installation in London, Ontario. Energy-efficient, quiet, zoned heating and cooling for homes without ductwork. Free quotes.",
   "problem_h":"Rooms that central air can't keep comfortable?",
   "problem_p":"London HVAC Pros installs ductless mini-split systems for efficient, zoned comfort that reaches the spaces a central system misses.",
   "features":[
     ("fan","Zoned Comfort Designed Around Your Home","Our certified technicians plan each ductless system around your layout, giving you independent control room by room, quiet operation, and high-efficiency performance from consultation through installation."),
     ("leaf","Efficient, Low-Disruption Installs","With no ductwork to run, a mini-split goes in faster and cleaner. Careful placement and sizing deliver strong efficiency ratings, flexible zoning, and lower energy bills all year."),
     ("shield","Licensed Installers You Can Rely On","Our licensed technicians install ductless mini-splits to spec with workmanship built to last, so you keep the energy savings and the comfort for the long run."),
   ],
   "rev":[1,4,2],
 },
 "heat-pump-repair-installation": {
   "icon":"refresh", "kicker":"Heat Pump Installation in London, ON",
   "h1":"Cold-Climate Heat Pump Installation for London Homes",
   "intro":"A heat pump heats and cools from one efficient system, and modern cold-climate models hold their own through an Ontario winter. London HVAC Pros installs heat pumps across London and the surrounding Middlesex County area, sizing each one to your home and, where it makes sense, pairing it with a backup furnace for the coldest days. It is one of the highest-impact efficiency upgrades a London home can make, and often a rebate-eligible one.",
   "meta":"Cold-climate heat pump installation in London, Ontario. Efficient year-round heating and cooling, rebate guidance, from licensed local technicians. Free quotes.",
   "problem_h":"Want one efficient system for heating and cooling?",
   "problem_p":"London HVAC Pros installs cold-climate heat pumps in London, Ontario for efficient year-round comfort and lower energy bills.",
   "features":[
     ("zap","Cold-Climate Systems, Properly Sized","We match your heat pump to your home with a load calculation and recommend a backup heat source where the climate calls for it, so you get efficient performance even on the coldest London nights."),
     ("leaf","One System, Lower Year-Round Bills","A heat pump replaces separate heating and cooling equipment and runs on far less energy than older systems. We walk you through the efficiency ratings and any rebates before you decide."),
     ("shield","Certified Install and Service","Our licensed technicians install and service every major heat pump brand to spec, with clear pricing and the upkeep that keeps efficiency high and the warranty intact."),
   ],
   "rev":[2,3,0],
 },
 "fireplace-installation": {
   "icon":"fireplace", "kicker":"Fireplace Installation in London, Ontario",
   "h1":"Efficient, Code-Compliant Fireplace Installation",
   "intro":"A modern gas fireplace adds zoned heat and a real design feature to a room, and an efficient unit gives you both without driving up your energy use. London HVAC Pros installs gas, electric, and wood-burning fireplaces across London, Ontario and the surrounding Middlesex County area, handling the venting, layout, and safety side so the finished install looks right and runs right.",
   "meta":"Professional gas, electric & wood-burning fireplace installation in London, Ontario. Efficient, safe, code-compliant and cleanly integrated. Free quotes.",
   "problem_h":"Want efficient zoned heat and a design feature?",
   "problem_p":"London HVAC Pros installs efficient, code-compliant fireplaces in London, cleanly integrated into your home and properly vented.",
   "features":[
     ("fireplace","Installation for Any Style","Whether you choose gas, electric, or wood-burning, our certified technicians plan the layout and venting and install the unit cleanly, giving the room an efficient heat source and a finished focal point."),
     ("shield","Safe and Code-Compliant Work","Every fireplace we install meets local building codes and safety standards, with proper venting, reliable operation, and the efficient heat output you expect from a modern unit."),
     ("award","Licensed Installers, Clean Finish","Our licensed technicians install your fireplace with transparent pricing and careful craftsmanship, so the result fits the room and performs for the long run."),
   ],
   "rev":[5,1,3],
 },
 "thermostat-repair-replacement": {
   "icon":"gauge", "kicker":"Smart Thermostat Installation in London, Ontario",
   "h1":"Smart Thermostat Upgrades and Replacement",
   "intro":"A smart thermostat is the easiest efficiency upgrade in most homes. London HVAC Pros installs programmable and smart thermostats across London, Ontario and the surrounding Middlesex County area, configuring each one to your HVAC system so it actually delivers the scheduling and energy savings it promises. We also repair and replace older controls that no longer hold an accurate temperature.",
   "meta":"Smart & programmable thermostat installation in London, Ontario. Configured to your HVAC system for real energy savings, by licensed techs. Free quote.",
   "problem_h":"Old thermostat costing you comfort and savings?",
   "problem_p":"An outdated thermostat wastes energy and leaves rooms uneven. We install and configure smart and programmable controls for efficient, reliable comfort.",
   "features":[
     ("settings","Smart Controls, Properly Configured","We install programmable and smart thermostats and set them up around your schedule and your HVAC equipment, so you see the scheduling, remote access, and energy savings rather than just the features."),
     ("gauge","Accurate Repair and Replacement","If a control short-cycles or reads the wrong temperature, we diagnose it precisely and repair or replace it, restoring consistent comfort and efficient operation across your system."),
     ("shield","Licensed Techs, Clear Pricing","Our licensed technicians install and service all thermostat brands, integrate them cleanly with your equipment, and quote the work up front with no surprises."),
   ],
   "rev":[4,0,5],
 },
 "duct-cleaning": {
   "icon":"air-vent", "kicker":"Duct Cleaning in London, ON",
   "h1":"Duct Cleaning to Protect System Efficiency and Air Quality",
   "intro":"A high-efficiency system can only perform as well as the ductwork moving air through it. London HVAC Pros provides thorough duct cleaning across London, Ontario and the surrounding Middlesex County communities, clearing the dust and buildup that restrict airflow, strain your equipment, and degrade the air you breathe. It is a smart step when you install new equipment or want your current system running at its rating.",
   "meta":"Professional air duct cleaning in London, Ontario. Restore airflow, protect system efficiency, improve air quality. Free quote from licensed local experts.",
   "problem_h":"Restricted airflow holding your system back?",
   "problem_p":"Dust and debris in ductwork choke airflow and pull your HVAC system below its rated efficiency. Our duct cleaning in London restores airflow and supports cleaner indoor air.",
   "features":[
     ("air-vent","Cleaner Air, Stronger Airflow","Our certified technicians use professional equipment to clear dust, pollen, and pet dander from ducts, vents, and air handlers, improving the air you breathe and letting your system move air the way it was designed to."),
     ("droplets","Protect Your Equipment Investment","Clean ducts ease the load on your furnace, air conditioner, or heat pump, helping a high-efficiency system hold its rating, run cooler, and last longer with fewer repairs."),
     ("shield","Licensed, Reliable Service","Our licensed technicians provide thorough duct cleaning with transparent pricing and cleaner air, so your home stays comfortable and your system stays efficient."),
   ],
   "rev":[0,2,4],
 },
}

REVIEW_POOL = [
  ("They had our furnace running again the same day — on one of the coldest nights of the year. Fast and professional.","Mya C.","London"),
  ("Fixed the problem quickly and explained everything clearly. Great service from start to finish.","Daniel P.","St. Thomas"),
  ("Reliable, affordable, and trustworthy. I won't call anyone else for HVAC.","Aisha N.","Strathroy"),
  ("Excellent response time and very knowledgeable technicians. Our home was comfortable again by morning.","Mark Z.","Dorchester"),
  ("Professional service, fair pricing, and no surprises. They made the whole process simple and stress-free.","Kevin H.","Komoka"),
  ("Friendly staff and outstanding workmanship. Our system runs better than ever after their visit.","Jennifer L.","Aylmer"),
]

def review_card(text, name, place):
    initials = "".join(w[0] for w in name.split()[:2]).upper()
    return f'''<article class="review reveal">
  {stars(5)}
  <p>&ldquo;{text}&rdquo;</p>
  <div class="review__by"><span class="av">{initials}</span><div><b>{name}</b><span>{place}, ON</span></div></div>
</article>'''

def feature_item(ic, h, p):
    return f'<li><span class="fi">{icon(ic,size=22)}</span><div><h4>{h}</h4><p>{p}</p></div></li>'

# ============================================================ SERVICE PAGE
def build_service(slug, data):
    url = f"/services/{slug}/"
    nav_label = next(s["nav"] for s in SERVICES if s["slug"]==slug)
    others = [s for s in SERVICES if s["slug"]!=slug]
    other_cards = "".join(
      f'''<a class="svc-card reveal" href="/services/{o["slug"]}/" style="padding:22px">
        <span class="svc-card__ic" style="width:48px;height:48px;margin-bottom:12px">{icon(o["icon"],size=24)}</span>
        <h3 style="font-size:1.05rem">{o["nav"]}</h3>
        <span class="svc-card__link" style="margin-top:10px">Learn more {icon('arrow-right',size=16)}</span>
      </a>''' for o in others)
    feats = "".join(feature_item(*f) for f in data["features"])
    revs = "".join(review_card(*REVIEW_POOL[i]) for i in data["rev"])
    breadcrumb_items = [("Home","/"),("Services","/services/"),(nav_label, url)]

    nav_plain = nav_label.replace("&amp;", "&")
    title = f"{nav_plain} in {CITY}, ON | {SITE_NAME}"
    if len(title) > 60:
        title = f"{nav_plain} | {CITY}, ON"

    out = head(
      title=title,
      desc=data["meta"], path=url, og_type="article",
      schema_blocks=[schema_localbusiness(),
                     schema_breadcrumb(breadcrumb_items),
                     schema_service(nav_label.replace('&amp;','and'), data["intro"], url)])

    out += f'''
<section class="page-hero">
  <div class="container">
    {crumbs([("Home","/"),("Services","/services/"),(nav_label,"")])}
    <span class="eyebrow on-dark">{data["kicker"]}</span>
    <h1>{data["h1"]}</h1>
    <p>{data["intro"]}</p>
    <div class="page-hero__cta">
      <a class="btn btn-primary btn-lg" href="#quote">Get a Free Quote</a>
      <a class="btn btn-ghost-light btn-lg" href="/services/">All Services</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="split">
      <div>
        <span class="eyebrow">Why Homeowners Call Us</span>
        <div class="callout reveal" style="margin-bottom:24px">
          <h3>{data["problem_h"]}</h3>
          <p>{data["problem_p"]}</p>
        </div>
        <ul class="feature-list">{feats}</ul>
      </div>
      <div class="split__media">
        <div style="position:sticky;top:96px">{quote_form(heading="Request Service", sub="Tell us what's going on — we'll get back to you fast.", id_suffix=slug)}</div>
      </div>
    </div>
  </div>
</section>

<section class="section bg-soft">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">Reviews</span>
      <h2>What London Homeowners Say</h2>
      <p>Real feedback from neighbours we've helped stay comfortable year-round.</p>
    </div>
    <div class="reviews">{revs}</div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">More Services</span>
      <h2>Explore Our Other HVAC Services</h2>
    </div>
    <div class="svc-grid">{other_cards}</div>
  </div>
</section>

{cta_band(title="We Can Help Solve Your "+nav_label.replace('&amp;','&')+" Needs",
          text="Don't let a comfort problem disrupt your home. Get fast, reliable service from London's trusted local HVAC team.")}
'''
    out += page_end()
    write(url, out)

# ============================================================ HOME
HOME_SERVICES = [
 ("flame","Furnace Installation &amp; Repair","Keep your home warm all winter with expert furnace repair and installation. From emergency calls to routine maintenance, we keep your system safe and efficient.","/services/furnace-repair/"),
 ("snowflake","AC Installation &amp; Repair","Beat the heat with reliable AC repair for central and ductless systems — fast diagnostics, tune-ups, and replacements to keep you cool all summer.","/services/ac-repair/"),
 ("refresh","Heat Pumps","Year-round, energy-efficient heating and cooling. We help you select, install, and maintain heat pump systems that lower energy costs and boost comfort.","/services/heat-pump-repair-installation/"),
 ("air-vent","Duct Cleaning","Remove dust, allergens, and debris from your ductwork to improve airflow, system efficiency, and the indoor air your family breathes.","/services/duct-cleaning/"),
 ("gauge","Thermostats","Smart and programmable thermostat repair and replacement for better temperature control, scheduling, and real energy savings.","/services/thermostat-repair-replacement/"),
 ("fan","Ductless AC Installation","Ideal for homes without ductwork — targeted, energy-efficient cooling and heating designed precisely around your space.","/services/ductless-ac-installation/"),
]

HOME_FAQ = [
 ("How much can a high-efficiency furnace or AC actually save me?","It depends on the equipment you have now, but moving from an older mid-efficiency furnace to a high-efficiency model often cuts heating gas use noticeably, and a properly sized AC runs less to hold the same temperature. We show you the projected operating costs before you choose."),
 ("What size system does my London home need?","The right size comes from a load calculation, not a rule of thumb. We measure your home, factor in insulation, windows, and layout, then recommend equipment that matches it. Oversized systems short-cycle and wear out early; undersized ones never keep up."),
 ("Do heat pumps work through a London winter?","Yes. Cold-climate heat pumps are rated to keep heating well below freezing, and we can pair one with a backup furnace for the coldest stretches. They also cool in summer, so one system covers both seasons efficiently."),
 ("Are there rebates available on a high-efficiency upgrade?","Often, yes. Rebate programs for high-efficiency furnaces, heat pumps, and smart thermostats change over time, so we check current eligibility for your project and help you choose equipment that qualifies."),
 ("Can a smart thermostat improve a new system's efficiency?","It helps. A programmable or smart thermostat lets a high-efficiency system run on a schedule that fits your day, and we configure it to your new equipment so you see the savings rather than just the features."),
 ("How long does a furnace or AC installation take?","Most residential furnace or AC replacements are a single day. Heat pump conversions or jobs that need ductwork changes can run longer. We give you a clear timeline up front and keep your home livable while we work."),
 ("Do you install ductless mini-split systems?","Yes. Ductless mini-splits are an efficient way to heat and cool additions, finished basements, or homes without ductwork. We design the zoning around how you use each room so no space is over- or under-conditioned."),
 ("Are your installers licensed and insured?","Every technician is fully licensed, insured, and trained on the high-efficiency equipment we install. Your system is fitted to manufacturer spec and local code so the warranty stays intact."),
 ("Do you serve areas outside of London, Ontario?",f"Yes. We serve London and nearby communities including {', '.join([a for a in SERVICE_AREAS if a!=CITY][:4])}, and the surrounding area."),
 ("Do you offer free quotes on a new system?","We do. New-system consultations come with a free, no-obligation quote that spells out the equipment, the efficiency rating, the install timeline, and any rebates you qualify for before you commit."),
]

def home_service_card(ic, title, text, url):
    return f'''<article class="svc-card reveal">
  <span class="svc-card__ic">{icon(ic,size=30)}</span>
  <h3>{title}</h3>
  <p>{text}</p>
  <a class="svc-card__link" href="{url}">Learn more {icon('arrow-right',size=17)}</a>
</article>'''

def faq_item(q,a):
    return f'''<details class="faq__item">
  <summary class="faq__q">{q}<span class="pm">{icon('chev-down',size=18)}</span></summary>
  <div class="faq__a"><p>{a}</p></div>
</details>'''

def build_home():
    cards = "".join(home_service_card(*c) for c in HOME_SERVICES)
    faqs = "".join(faq_item(q,a) for q,a in HOME_FAQ)
    revs = "".join(review_card(*r) for r in [
      ("The team saved us with an emergency furnace repair in January. Professional, friendly, and they truly cared about our comfort.","Sarah M.","London"),
      ("Best team for HVAC! They helped us choose an energy-efficient AC system without upselling unnecessary equipment.","David R.","St. Thomas"),
      ("Prompt, polite, and knowledgeable. They handled our heat pump installation with real pride. Highly recommend.","Jennifer T.","Strathroy"),
    ])
    blog_cards = build_blog_cards(BLOG)

    out = head(
      title=f"{SITE_NAME} — HVAC Company in {CITY}, ON",
      desc=f"Honest, efficient, dependable HVAC service in {CITY}, Ontario — furnace & AC repair, heat pumps & more. Call {PHONE_DISPLAY} for a free quote.",
      path="/",
      schema_blocks=[schema_localbusiness(), schema_faq(HOME_FAQ)])

    out += f'''
<section class="{hero_class()}">
  <div class="hero__glow"></div>
  <div class="container">
    <div class="hero__copy reveal">
      <span class="eyebrow on-dark">{CITY}'s High-Efficiency HVAC Installers</span>
      <h1>New Furnace, AC &amp; Heat Pump Installs in <span class="accent">{CITY}, ON</span></h1>
      <p class="hero__sub">{SITE_NAME} designs and installs high-efficiency heating and cooling systems for homes across {CITY}, Ontario and {COUNTY}. Right-sized equipment, certified workmanship, and the rebate guidance to make the upgrade pay off.</p>
      <div class="hero__cta">
        <a class="btn btn-primary btn-lg" href="#quote">Get a Free Quote</a>
        <a class="btn btn-ghost-light btn-lg" href="/services/">Explore Our Services</a>
      </div>
      <ul class="hero__trust">
        <li>{icon('check',size=22)} 24/7 HVAC Service</li>
        <li>{icon('check',size=22)} Financing Options</li>
        <li>{icon('check',size=22)} 100% Satisfaction Guaranteed</li>
        <li>{icon('check',size=22)} Licensed &amp; Insured</li>
      </ul>
    </div>
    <div class="hero__form reveal d1">{quote_form()}</div>
  </div>
</section>

<section class="trust-strip">
  <div class="container">
    <div class="trust-strip__item"><span class="ic">{icon('clock',size=26)}</span><div><b>24/7</b><span>Emergency service</span></div></div>
    <div class="trust-strip__item"><span class="ic">{icon('shield',size=26)}</span><div><b>Licensed</b><span>&amp; fully insured</span></div></div>
    <div class="trust-strip__item"><span class="ic">{icon('dollar',size=26)}</span><div><b>Free</b><span>No-obligation quotes</span></div></div>
    <div class="trust-strip__item"><span class="ic">{icon('users',size=26)}</span><div><b>Local</b><span>Family-run &amp; trusted</span></div></div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="split">
      <div class="reveal">
        <span class="eyebrow">Installation Specialists</span>
        <h2>High-Efficiency System Upgrades, Done Right the First Time</h2>
        <p class="lead">London HVAC Pros is a licensed HVAC company in London, Ontario that specializes in installing high-efficiency furnaces, air conditioners, and heat pumps. We focus on the upgrade itself: choosing the right system, sizing it correctly, and installing it to last.</p>
        <p>A new system is only as good as the load calculation behind it. We measure your home, match equipment to it instead of guessing, and walk you through the efficiency ratings and available rebates before you commit. The result is lower operating costs, even comfort in every room, and an install that holds up for years.</p>
        <div style="display:flex;gap:14px;flex-wrap:wrap;margin-top:8px">
          <a class="btn btn-secondary" href="/about/">More About Us</a>
          <a class="btn btn-outline" href="/contact/">Contact the Team</a>
        </div>
      </div>
      <div class="split__media reveal d1">
        <div class="media-panel">
          <div class="media-panel__row">
            <div class="media-chip warm"><span class="ic">{icon('flame',size=24)}</span><b>Heating</b><span>Furnaces, heat pumps &amp; fireplaces</span></div>
            <div class="media-chip cool"><span class="ic">{icon('snowflake',size=24)}</span><b>Cooling</b><span>Central air &amp; ductless systems</span></div>
            <div class="media-chip cool"><span class="ic">{icon('droplets',size=24)}</span><b>Air Quality</b><span>Duct cleaning &amp; ventilation</span></div>
            <div class="media-chip warm"><span class="ic">{icon('gauge',size=24)}</span><b>Controls</b><span>Smart &amp; programmable thermostats</span></div>
            <div class="media-chip media-chip--wide cool" style="display:flex;align-items:center;gap:14px">
              <span class="ic" style="margin:0">{icon('headset',size=24)}</span>
              <div><b>Real local technicians, on call 24/7</b><span>Serving London &amp; Middlesex County, every day of the year</span></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section bg-soft">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">Installations &amp; Upgrades</span>
      <h2>High-Efficiency Heating &amp; Cooling Systems for London Homes</h2>
      <p>We install and service the full range of modern HVAC equipment, from high-efficiency furnaces and central air to cold-climate heat pumps and smart controls, all sized and fitted to your home.</p>
    </div>
    <div class="svc-grid">{cards}</div>
    <div class="center" style="margin-top:34px">
      <a class="btn btn-primary btn-lg reveal" href="/services/">View All Services {icon('arrow-right',size=18)}</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">Our Process</span>
      <h2>How We Plan Your System Upgrade</h2>
      <p>A good install starts long before the new equipment arrives. Here is how we take a project from first visit to lasting comfort.</p>
    </div>
    <div class="steps">
      <div class="step reveal"><div class="step__ic">{icon('search',size=26)}</div><div class="step__num"></div><h3>Home Assessment &amp; Sizing</h3><p>We measure your home and run a proper load calculation so your new furnace, AC, or heat pump is matched to the space, then lay out your efficiency options and rebate eligibility in plain numbers.</p></div>
      <div class="step reveal d1"><div class="step__ic">{icon('wrench',size=26)}</div><div class="step__num"></div><h3>Precise, Clean Installation</h3><p>Certified technicians install your system to manufacturer spec and local code, set it up for peak efficiency, and leave your home as tidy as they found it.</p></div>
      <div class="step reveal d2"><div class="step__ic">{icon('headset',size=26)}</div><div class="step__num"></div><h3>Commissioning &amp; Follow-Up</h3><p>Before we leave we test airflow and performance, walk you through the controls, and stay on hand for tune-ups that protect your investment and warranty for years.</p></div>
    </div>
  </div>
</section>

<section class="section bg-soft">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">Testimonials</span>
      <h2>What London Homeowners Are Saying</h2>
      <p>We're proud to be the heating and cooling partner our neighbours trust and recommend.</p>
    </div>
    <div class="reviews">{revs}</div>
  </div>
</section>

{cta_band(title="Ready to Improve Your Home Comfort?",
          text="No matter the make or model, our experts have the tools and experience to handle any furnace, air conditioner, heat pump, or ventilation issue — fast.")}

<section class="section">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">From the Blog</span>
      <h2>Latest News &amp; Home Comfort Tips</h2>
      <p>Practical advice to help you get the most from your heating and cooling system in London's climate.</p>
    </div>
    <div class="post-grid">{blog_cards}</div>
  </div>
</section>

<section class="section bg-soft">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">FAQs</span>
      <h2>Frequently Asked Questions</h2>
      <p>Answers to the questions London homeowners ask us most.</p>
    </div>
    <div class="faq">{faqs}</div>
  </div>
</section>

{areas_section()}
'''
    out += page_end()
    write("/", out)

# ============================================================ SERVICES INDEX
def build_services_index():
    cards = "".join(
      f'''<article class="svc-card reveal">
        <span class="svc-card__ic">{icon(s["icon"],size=30)}</span>
        <h3>{s["nav"]}</h3>
        <p>{SVC[s["slug"]]["problem_p"]}</p>
        <a class="svc-card__link" href="/services/{s["slug"]}/">Learn more {icon('arrow-right',size=17)}</a>
      </article>''' for s in SERVICES)
    out = head(
      title=f"HVAC Services in {CITY}, ON | {SITE_NAME}",
      desc=f"Full-service heating & cooling in London, Ontario — furnace & AC repair, heat pumps, ductless AC, thermostats & duct cleaning. Free quotes.",
      path="/services/",
      schema_blocks=[schema_localbusiness(), schema_breadcrumb([("Home","/"),("Services","/services/")])])
    out += f'''
<section class="page-hero">
  <div class="container">
    {crumbs([("Home","/"),("Services","")])}
    <span class="eyebrow on-dark">Our Services</span>
    <h1>Complete HVAC Services for London Homes</h1>
    <p>From emergency repairs to new installations and seasonal maintenance, we keep your home comfortable in every season. Explore our full range of heating, cooling, and air-quality services below.</p>
    <div class="page-hero__cta">
      <a class="btn btn-primary btn-lg" href="/contact/">Get a Free Quote</a>
      <a class="btn btn-ghost-light btn-lg" href="/about/">Why Choose Us</a>
    </div>
  </div>
</section>
<section class="section">
  <div class="container"><div class="svc-grid">{cards}</div></div>
</section>
<section class="section bg-soft">
  <div class="container">
    <div class="steps">
      <div class="step reveal"><div class="step__ic">{icon('clock',size=26)}</div><div class="step__num"></div><h3>24/7 Emergency Service</h3><p>Heating and cooling failures don't wait for business hours. Our team is on call around the clock for London and Middlesex County.</p></div>
      <div class="step reveal d1"><div class="step__ic">{icon('shield',size=26)}</div><div class="step__num"></div><h3>Licensed &amp; Insured</h3><p>Every technician is fully licensed, insured, and trained to service all major HVAC brands and high-efficiency systems.</p></div>
      <div class="step reveal d2"><div class="step__ic">{icon('dollar',size=26)}</div><div class="step__num"></div><h3>Honest, Upfront Pricing</h3><p>Free, no-obligation quotes and clear pricing before any work begins — no surprises, no pressure, no upselling.</p></div>
    </div>
  </div>
</section>
{cta_band()}
'''
    out += page_end()
    write("/services/", out)

# ============================================================ ABOUT
def build_about():
    out = head(
      title=f"About Us | {SITE_NAME}",
      desc=f"London HVAC Pros is a local, family-run HVAC company serving London, Ontario with honest, reliable heating and cooling care. Meet the team.",
      path="/about/",
      schema_blocks=[schema_localbusiness(), schema_breadcrumb([("Home","/"),("About","/about/")])])
    out += f'''
<section class="page-hero">
  <div class="container">
    {crumbs([("Home","/"),("About","")])}
    <span class="eyebrow on-dark">About Us</span>
    <h1>A Local Tradition of Home Comfort</h1>
    <p>We aren't just technicians — we're your neighbours, committed to keeping London families comfortable through every season.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="split">
      <div class="reveal">
        <span class="eyebrow">Our Story</span>
        <h2>People Over Profits, Season After Season</h2>
        <p>At London HVAC Pros, we believe every family deserves a comfortable, healthy home. As a family-oriented business based in London, Ontario, our mission is simple: keep your home comfortable through every season with the same high standard of care we'd expect for our own households.</p>
        <p>Our journey began with one goal — to provide honest, transparent home services that put people first. We know that when your furnace or air conditioner fails, it's more than an inconvenience; it's a disruption to your family's peace of mind. That's why we've built our reputation on being a reliable HVAC company that delivers tailored solutions with a personal touch.</p>
      </div>
      <div class="split__media reveal d1">
        <div class="media-panel">
          <div class="media-panel__row">
            <div class="media-chip warm"><span class="ic">{icon('users',size=24)}</span><b>Family-Run</b><span>Locally owned &amp; operated</span></div>
            <div class="media-chip cool"><span class="ic">{icon('shield',size=24)}</span><b>Licensed</b><span>Insured &amp; certified techs</span></div>
            <div class="media-chip cool"><span class="ic">{icon('leaf',size=24)}</span><b>Efficient</b><span>Energy-saving systems</span></div>
            <div class="media-chip warm"><span class="ic">{icon('clock',size=24)}</span><b>Available</b><span>24/7 emergency service</span></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section bg-soft">
  <div class="container">
    <div class="split reverse">
      <div class="split__media reveal">
        <div class="callout"><h3>Why London Families Trust Us</h3><p>We specialize in everything from high-efficiency furnace installation to complex central-air diagnostics. Our team handles both residential and light-commercial systems, so whether you're at home or at work, your environment stays perfectly regulated.</p></div>
      </div>
      <div class="reveal d1">
        <span class="eyebrow">Our Commitment</span>
        <h2>Comfort, Integrity &amp; Indoor Air Quality</h2>
        <p>We take pride in our expertise in energy-efficient air conditioning and modern heating, helping our community reduce its carbon footprint while saving on monthly utility bills.</p>
        <p>When you choose us, you aren't just getting a repair service — you're joining a community of satisfied homeowners who value quality, integrity, and a heating and cooling partner who genuinely cares.</p>
        <ul class="feature-list">
          {feature_item('check-sm','Honest, Transparent Pricing','Free quotes and clear estimates before any work starts.')}
          {feature_item('check-sm','Trained, Courteous Technicians','On-time, tidy, and respectful of your home.')}
          {feature_item('check-sm','Standing Behind Our Work','100% satisfaction guarantee on every job.')}
        </ul>
      </div>
    </div>
  </div>
</section>

{cta_band(title="Experience the London HVAC Pros Difference",
          text="Join your neighbours who count on us for honest, dependable home comfort. Reach out for your free quote today.")}
{areas_section()}
'''
    out += page_end()
    write("/about/", out)

# ============================================================ CONTACT
def build_contact():
    out = head(
      title=f"Contact Us | {SITE_NAME}",
      desc=f"Contact London HVAC Pros for fast, friendly HVAC service in London, Ontario. Call {PHONE_DISPLAY} or request a free quote online. Open 24/7.",
      path="/contact/",
      schema_blocks=[schema_localbusiness(), schema_breadcrumb([("Home","/"),("Contact","/contact/")])])
    out += f'''
<section class="page-hero">
  <div class="container">
    {crumbs([("Home","/"),("Contact","")])}
    <span class="eyebrow on-dark">Contact Us</span>
    <h1>Let's Get Your Comfort Back on Track</h1>
    <p>Is your air conditioner making a strange noise? Ready to upgrade your furnace before winter? Whatever your home comfort need, the London HVAC Pros team is ready to help — without the stress.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="info-grid" style="margin-bottom:40px">
      <div class="info-card reveal"><span class="ic">{icon('clock',size=26)}</span><h3>Fast Response</h3><p>We reply within one business day</p><p style="color:var(--muted);font-size:.9rem;margin-top:4px">Same-day service for emergencies</p></div>
      <div class="info-card reveal d1"><span class="ic">{icon('mail',size=26)}</span><h3>Email Us</h3><p><a href="mailto:{EMAIL}">{EMAIL}</a></p><p style="color:var(--muted);font-size:.9rem;margin-top:4px">We reply within one business day</p></div>
      <div class="info-card reveal d2"><span class="ic">{icon('pin',size=26)}</span><h3>Service Area</h3><p>{CITY}, {REGION}, {ADDR_POSTAL}</p><p style="color:var(--muted);font-size:.9rem;margin-top:4px">Serving London &amp; Middlesex County</p></div>
    </div>
    <div class="split">
      <div class="reveal">
        <span class="eyebrow">Send a Message</span>
        <h2>Request Your Free Quote</h2>
        <p>Fill out the form and one of our friendly local technicians will get back to you quickly to discuss your heating or cooling needs. For urgent issues, calling is always fastest.</p>
        <ul class="feature-list" style="margin-top:24px">
          {feature_item('clock','Fast Response','We prioritise emergency calls and aim to respond the same day.')}
          {feature_item('dollar','Free, No-Obligation Quotes','Know your options and pricing before committing to anything.')}
          {feature_item('shield','Licensed &amp; Insured','Professional, certified service you can trust in your home.')}
        </ul>
      </div>
      <div class="split__media reveal d1">{quote_form(heading="Get a Free Quote", sub="Tell us about your heating or cooling issue.", id_suffix="contact")}</div>
    </div>
  </div>
</section>

<section class="section bg-soft">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">Service Hours</span>
      <h2>We're Here Whenever You Need Us</h2>
      <p>Heating and cooling emergencies don't keep a schedule — and neither do we.</p>
    </div>
    <div class="info-grid">
      <div class="info-card center reveal"><span class="ic" style="margin-inline:auto">{icon('clock',size=26)}</span><h3>24 Hours a Day</h3><p style="color:var(--muted)">Round-the-clock emergency service</p></div>
      <div class="info-card center reveal d1"><span class="ic" style="margin-inline:auto">{icon('calendar',size=26)}</span><h3>7 Days a Week</h3><p style="color:var(--muted)">Including weekends &amp; holidays</p></div>
      <div class="info-card center reveal d2"><span class="ic" style="margin-inline:auto">{icon('headset',size=26)}</span><h3>Real Local People</h3><p style="color:var(--muted)">Speak with a London technician</p></div>
    </div>
  </div>
</section>

{areas_section()}
'''
    out += page_end()
    write("/contact/", out)

# ============================================================ BLOG
BLOG = [
 {"slug":"how-often-should-you-service-your-hvac-system-in-london-ontario",
  "title":"How Often Should You Service Your HVAC System in London, Ontario?",
  "seo_title":"How Often to Service Your HVAC in London, ON",
  "date":"2026-01-12","date_h":"January 12, 2026","img":"cool","icon":"calendar",
  "excerpt":"London's real seasons push your HVAC system hard. Here's how often you should service your furnace and AC — and why twice a year is the sweet spot.",
  "meta":"How often should you service your HVAC system in London, Ontario? Learn the ideal furnace and AC maintenance schedule for our climate from local experts.",
  "body":None},
 {"slug":"signs-your-furnace-needs-repair-before-a-london-winter",
  "title":"Signs Your Furnace Needs Repair Before a London Winter",
  "seo_title":"Signs Your Furnace Needs Repair Before Winter",
  "date":"2026-02-15","date_h":"February 15, 2026","img":"warm","icon":"flame",
  "excerpt":"Don't wait for the coldest night of the year. Here are the most common warning signs your furnace needs repair before a London winter sets in.",
  "meta":"Five warning signs your furnace needs repair before a London, Ontario winter — strange noises, uneven heat, rising bills and more. Stay warm and safe.",
  "body":None},
 {"slug":"why-your-air-conditioner-struggles-during-humid-london-summers",
  "title":"Why Your Air Conditioner Struggles During Humid London Summers",
  "seo_title":"Why Your AC Struggles in Humid London Summers",
  "date":"2026-03-09","date_h":"March 9, 2026","img":"cool","icon":"droplets",
  "excerpt":"If your AC runs all day but your home still feels sticky, humidity is likely the culprit. Here's why — and what you can do about it.",
  "meta":"Why does your air conditioner struggle in humid London summers? Learn how humidity affects cooling and what AC service near Lake Erie can do to help.",
  "body":None},
]

def build_blog_cards(posts, limit=3):
    out=""
    for p in posts[:limit]:
        out += f'''<article class="post-card reveal">
  <div class="post-card__img {p["img"]}">{icon(p["icon"],size=54)}</div>
  <div class="post-card__body">
    <span class="tag">Home Comfort Tips</span>
    <h3>{p["title"]}</h3>
    <p>{p["excerpt"]}</p>
    <a class="post-card__link" href="/blog/{p["slug"]}/">Read article {icon('arrow-right',size=17)}</a>
  </div>
</article>'''
    return out

def build_blog_index():
    cards = build_blog_cards(BLOG, limit=len(BLOG))
    out = head(
      title=f"HVAC Tips &amp; Home Comfort Blog | {SITE_NAME}",
      desc="Practical heating and cooling advice for London, Ontario homeowners — maintenance schedules, furnace warning signs, humidity tips and more.",
      path="/blog/",
      schema_blocks=[schema_localbusiness(), schema_breadcrumb([("Home","/"),("Blog","/blog/")])])
    out += f'''
<section class="page-hero">
  <div class="container">
    {crumbs([("Home","/"),("Blog","")])}
    <span class="eyebrow on-dark">Our Blog</span>
    <h1>News &amp; Home Comfort Tips</h1>
    <p>Straightforward advice to help you get the most out of your heating and cooling system in London's climate.</p>
  </div>
</section>
<section class="section">
  <div class="container"><div class="post-grid">{cards}</div></div>
</section>
{cta_band()}
'''
    out += page_end()
    write("/blog/", out)

def article_shell(p, body_html):
    related = [x for x in BLOG if x["slug"]!=p["slug"]]
    rel_cards = build_blog_cards(related, limit=2)
    url=f"/blog/{p['slug']}/"
    seo_title = p.get("seo_title", p["title"])  # concise <title> (<=60 chars); H1 keeps full headline
    out = head(title=seo_title, desc=p["meta"], path=url, og_type="article",
      schema_blocks=[schema_localbusiness(),
                     schema_breadcrumb([("Home","/"),("Blog","/blog/"),(p["title"], url)]),
                     schema_blogpost(p["title"], p["meta"], url, p["date"])])
    out += f'''
<section class="page-hero">
  <div class="container">
    {crumbs([("Home","/"),("Blog","/blog/"),(p["title"][:42]+"…","")])}
    <div class="article__meta" style="color:#9fb9d4"><span class="tag">Home Comfort Tips</span>{icon('calendar',size=16)} {p["date_h"]}</div>
    <h1>{p["title"]}</h1>
  </div>
</section>
<section class="section">
  <div class="container">
    <article class="article reveal">{body_html}
      <div class="note-banner" style="margin-top:30px;background:var(--bg-alt);border:1px solid var(--line);color:var(--body)">
        <strong style="color:var(--navy-900)">Need help now?</strong>
        <a href="/contact/">Request a free quote</a> and a local London technician will get back to you fast — we're here 24/7.
      </div>
    </article>
  </div>
</section>
<section class="section bg-soft">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">Keep Reading</span><h2>More Home Comfort Tips</h2></div>
    <div class="post-grid">{rel_cards}</div>
  </div>
</section>
{cta_band()}
'''
    out += page_end()
    write(url, out)

def build_blog_posts():
    bodies = blog_bodies()
    for p in BLOG:
        article_shell(p, bodies[p["slug"]])

# ---- Blog bodies (localized) ----
def blog_bodies():
    return {
 "how-often-should-you-service-your-hvac-system-in-london-ontario": '''
<p class="lead">Living in London, Ontario means dealing with real seasons. Winter can be bitterly cold, and summer near Lake Erie brings long stretches of heat and humidity. Your HVAC system doesn't get much of a break — which is exactly why regular maintenance matters.</p>
<p>At London HVAC Pros, we often hear the same question: <em>how often should I service my heating and cooling system?</em> Our answer is simple. At minimum, twice per year.</p>
<h2>Why Regular HVAC Service Is So Important</h2>
<p>Your furnace and air conditioner run for thousands of hours every year. Over time, dust builds up inside the system, filters get clogged, electrical connections loosen, and moving parts wear down. None of this happens overnight, which is why problems can go unnoticed until something suddenly stops working.</p>
<p>When maintenance is skipped, homeowners often notice higher energy bills, uneven temperatures from room to room, poor airflow, or air that feels dusty and stale. Small issues that could have been corrected during a routine visit can turn into expensive repairs at the worst possible time.</p>
<p>Regular service lets a technician catch those small concerns early. It keeps your system running efficiently and helps prevent breakdowns during peak heating or cooling season — when you need it most.</p>
<h2>The Ideal Service Schedule in Ontario</h2>
<p>In our climate, servicing your HVAC system twice a year makes the most sense: once in the spring before summer arrives, and once in the fall before winter sets in.</p>
<h3>Spring Air Conditioning Tune-Up</h3>
<p>Before the hot weather hits London, your air conditioner should be inspected and cleaned. After sitting idle all winter, components may need attention. A spring tune-up ensures your system is ready to handle long, humid days without struggling.</p>
<p>During a typical cooling service, a technician will check refrigerant levels, clean the outdoor condenser unit, inspect electrical components, test the thermostat, and make sure airflow is strong and balanced. When your AC is clean and properly adjusted, it cools your home more effectively and uses less energy to do it.</p>
<h3>Fall Furnace Inspection</h3>
<p>Before temperatures drop, your heating system should be checked for both performance and safety. In Canada, a reliable furnace isn't just about comfort — it's about protecting your home and family during freezing conditions.</p>
<p>A fall heating inspection typically includes examining the heat exchanger, checking gas connections, testing ignition systems, cleaning burners, and ensuring there are no carbon monoxide concerns. Filters are replaced and airflow is verified, helping your furnace run safely throughout the winter.</p>
<h2>The Long-Term Benefits</h2>
<p>Homeowners who stay consistent with HVAC maintenance usually notice lower utility costs and fewer emergency repair calls. Systems that are properly maintained tend to last longer and perform better throughout their lifespan. There's also the benefit of better indoor air quality — clean components and fresh filters reduce dust circulation and help your home feel healthier.</p>
<p>Think of HVAC maintenance the same way you think about servicing your vehicle. Routine care may seem small, but it plays a major role in avoiding larger problems later.</p>
<h2>Don't Wait Until Something Fails</h2>
<p>Many service calls happen in the middle of a heat wave or during a cold snap. By then, the system has already been under stress for weeks. Preventative maintenance is far more affordable — and far less stressful — than emergency repairs.</p>
<p>Scheduling service before each major season gives you peace of mind, knowing your system has been inspected, cleaned, and tested by a professional.</p>
<h2>Book Your Service With London HVAC Pros</h2>
<p>We're proud to serve homeowners throughout London and the surrounding Middlesex County area. As a local, family-operated company, we focus on honest service and long-term relationships with our customers. If it has been more than a year since your last HVAC service, now is the time to schedule.</p>
''',
 "signs-your-furnace-needs-repair-before-a-london-winter": '''
<p class="lead">Winter in London, Ontario is serious business. When temperatures fall well below freezing and the wind comes off Lake Erie, your furnace becomes the heart of your home. It keeps your family warm, protects your plumbing from freezing, and makes everyday life comfortable.</p>
<p>The problem is, many homeowners don't think about their furnace until it stops working — and by then, it's often the coldest week of the year. Catching early warning signs can help you avoid a complete heating failure when you need warmth the most.</p>
<h2>1. Your Furnace Is Making Strange Noises</h2>
<p>A properly working furnace should run relatively quietly. You might hear the gentle sound of air moving through vents or the system starting up, but loud or unusual noises are not normal.</p>
<p>If you hear banging, squealing, rattling, or grinding, it could mean loose internal parts, motor issues, or airflow problems. Sometimes it's as simple as a worn belt or a loose panel; other times it points to something more serious inside the blower assembly or burner system. The key is not to ignore it — small mechanical issues can quickly turn into bigger, more expensive repairs.</p>
<h2>2. Uneven Heating Around Your Home</h2>
<p>Do you notice that some rooms feel warm while others stay cold? Uneven heating is one of the most common complaints we hear from homeowners in London.</p>
<p>This may be caused by ductwork problems, restricted airflow, a struggling blower motor, or a thermostat that isn't reading temperatures accurately. Over time, these issues put extra strain on your furnace as it works harder to compensate. A professional inspection can pinpoint the cause and restore consistent heating throughout your home.</p>
<h2>3. Your Energy Bills Are Suddenly Higher</h2>
<p>If your heating bills jump significantly and the weather hasn't changed much, your furnace may be losing efficiency. When filters are clogged, burners are dirty, or internal components are worn, your system has to run longer to maintain the same temperature — and that extra runtime means higher costs.</p>
<p>Many homeowners assume rising bills are just part of winter in Ontario, but a sudden spike is often a sign your furnace needs attention.</p>
<h2>4. Frequent Cycling On and Off</h2>
<p>Does your furnace turn on, run briefly, then shut off, only to start again a few minutes later? This is known as short cycling.</p>
<p>Short cycling can be caused by a dirty filter, thermostat issues, overheating, or improper airflow. Not only does it reduce comfort, it increases wear and tear on your system — repeatedly starting and stopping stresses components and can shorten the life of your furnace. Addressing it early can prevent larger breakdowns later in the season.</p>
<h2>5. Yellow Pilot Light on a Gas Furnace</h2>
<p>If you have a gas furnace, the pilot flame should burn blue. A yellow or flickering flame may indicate improper combustion and, in some cases, a carbon monoxide risk.</p>
<p>This is not something to ignore. If you notice a yellow flame or suspect a combustion issue, have your system inspected by a licensed professional right away. Safety should always come first.</p>
<h2>Why Acting Early Matters</h2>
<p>Putting off furnace repairs can lead to a complete system breakdown during freezing temperatures. Emergency repairs in the middle of winter are not only stressful but can also be more costly. Taking care of small repairs now helps protect your furnace, extend its lifespan, and give you peace of mind before the coldest months arrive.</p>
<h2>Need Furnace Repair in London, Ontario?</h2>
<p>At London HVAC Pros, we understand how important reliable heat is for your home and family. As a local, family-operated HVAC company, we provide fast, dependable furnace repair throughout London and nearby Middlesex County communities. If you've noticed any of these warning signs, don't wait for winter to put your system to the test.</p>
''',
 "why-your-air-conditioner-struggles-during-humid-london-summers": '''
<p class="lead">If your air conditioner seems to run all day but your home still feels sticky and uncomfortable, you're not imagining it. Summers in London, Ontario aren't just hot — they're humid. Sitting close to Lake Erie, our area sees moisture levels that play a major role in how comfortable your home feels, even when the temperature looks fine.</p>
<p>Many homeowners assume their AC is failing when the real issue is excess moisture in the air. Understanding how your system works can help explain why it may be struggling.</p>
<h2>Your Air Conditioner Does More Than Just Cool</h2>
<p>An air conditioning system has two main jobs: it lowers the temperature and it removes moisture from the air. When humidity levels rise, your system has to work much harder to keep your home comfortable.</p>
<p>High humidity makes the air feel heavier and warmer than it actually is. That's why 26 degrees on a dry day feels very different from 26 degrees during a humid stretch in July. When moisture levels are high, your AC runs longer cycles trying to pull that extra humidity out of the air — and if something isn't working properly, it may never quite catch up.</p>
<h2>Common Reasons Your AC Can't Keep Up</h2>
<p>Several issues can reduce your air conditioner's ability to handle both heat and humidity:</p>
<ul class="bullets">
  <li><strong>Dirty air filters.</strong> When filters are clogged, airflow becomes restricted, and without proper airflow your system cannot cool or dehumidify effectively.</li>
  <li><strong>Low refrigerant levels.</strong> Refrigerant is what allows your system to remove heat from your home. If levels are low due to a leak or improper charge, cooling efficiency drops.</li>
  <li><strong>Dirty coils.</strong> Over time, dust and debris build up on the evaporator and condenser coils, preventing proper heat exchange and making it harder to remove both heat and moisture.</li>
  <li><strong>Leaky ductwork.</strong> If cooled air escapes before it reaches your living spaces, your system runs longer trying to reach the thermostat setting.</li>
  <li><strong>An undersized system.</strong> If the unit wasn't properly sized during installation, it may struggle during peak summer conditions in London.</li>
</ul>
<h2>The Impact of High Indoor Humidity</h2>
<p>When humidity isn't controlled, your home can feel sticky even when the temperature seems reasonable. High moisture levels can also contribute to mold growth, musty odors, and added strain on your HVAC system. Over time, excessive humidity can even affect wood floors, furniture, and overall indoor air quality — which is why proper AC performance is about more than just comfort.</p>
<h2>How Professional AC Service Helps</h2>
<p>Regular professional maintenance can make a significant difference during humid weather. A thorough air conditioning service typically includes cleaning the coils, checking refrigerant levels, testing airflow, calibrating the thermostat, and evaluating overall system performance. When the system is clean and properly adjusted, it cools faster, runs more efficiently, and maintains better indoor comfort.</p>
<h2>Don't Let Your System Run Nonstop</h2>
<p>If your air conditioner is running constantly but your home still feels uncomfortable, it's a sign something needs attention. Letting the system run nonstop not only increases your energy bills but can also shorten the lifespan of the equipment. Addressing the issue early can prevent larger repairs later in the season.</p>
<h2>Schedule AC Service in London Today</h2>
<p>At London HVAC Pros, we understand how challenging Ontario summers can be. As a family-owned and operated HVAC company, we provide honest, reliable air conditioning repair and maintenance throughout London and the surrounding Middlesex County area. If your home feels humid or your AC is struggling to keep up, we'll help restore comfort and keep your cooling system running efficiently all summer long.</p>
''',
    }

# ============================================================ PRIVACY + 404
def build_privacy():
    out = head(title=f"Privacy Policy | {SITE_NAME}",
      desc="Privacy policy for London HVAC Pros — how we collect, use, and protect your personal information.",
      path="/privacy-policy/",
      schema_blocks=[schema_breadcrumb([("Home","/"),("Privacy Policy","/privacy-policy/")])])
    out += f'''
<section class="page-hero">
  <div class="container">
    {crumbs([("Home","/"),("Privacy Policy","")])}
    <span class="eyebrow on-dark">Legal</span>
    <h1>Privacy Policy</h1>
    <p>Last updated: <span data-year>2026</span></p>
  </div>
</section>
<section class="section">
  <div class="container">
    <article class="article">
      <p class="lead">{SITE_NAME} ("we," "us," or "our") respects your privacy. This policy explains what information we collect when you use our website or request our services, and how we use and protect it.</p>
      <h2>Information We Collect</h2>
      <p>When you submit a quote request or contact form, we collect the information you provide — such as your name, phone number, email address, service address, and a description of your heating or cooling needs. We may also collect basic, non-identifying analytics data about how visitors use our site.</p>
      <h2>How We Use Your Information</h2>
      <p>We use the information you provide to respond to your enquiry, schedule and deliver services, provide quotes, and follow up about your home comfort needs. We do not sell or rent your personal information to third parties.</p>
      <h2>How We Protect Your Information</h2>
      <p>We take reasonable measures to protect the personal information you share with us against loss, theft, and unauthorized access. Information is shared only with team members and trusted service partners who need it to serve you.</p>
      <h2>Cookies &amp; Analytics</h2>
      <p>Our website may use cookies and similar technologies to improve your browsing experience and understand site usage. You can disable cookies through your browser settings, though some features may not function as intended.</p>
      <h2>Your Choices</h2>
      <p>You may request access to, correction of, or deletion of the personal information we hold about you at any time by contacting us using the details below.</p>
      <h2>Contact Us</h2>
      <p>If you have questions about this privacy policy or how your information is handled, please reach out:</p>
      <p>{SITE_NAME}<br>Email: <a href="mailto:{EMAIL}">{EMAIL}</a><br>{CITY}, {REGION}, {ADDR_POSTAL}</p>
    </article>
  </div>
</section>
'''
    out += page_end()
    write("/privacy-policy/", out)

def build_404():
    out = head(title=f"Page Not Found | {SITE_NAME}", desc="The page you're looking for could not be found.",
               path="/404.html", robots="noindex, follow")
    out += f'''
<section class="page-hero">
  <div class="container center">
    <span class="eyebrow on-dark" style="justify-content:center">Error 404</span>
    <h1>This Page Took a Wrong Turn</h1>
    <p style="margin-inline:auto">The page you're looking for doesn't exist or may have moved. Let's get you back to comfort.</p>
    <div class="page-hero__cta" style="justify-content:center">
      <a class="btn btn-primary btn-lg" href="/">Back to Home</a>
      <a class="btn btn-ghost-light btn-lg" href="/services/">View Services</a>
    </div>
  </div>
</section>
<section class="section"><div class="container">
  <div class="section-head"><span class="eyebrow">Popular Pages</span><h2>Where Would You Like to Go?</h2></div>
  <div class="svc-grid">
    {''.join(f'<a class="svc-card" href="/services/{s["slug"]}/"><span class="svc-card__ic">{icon(s["icon"],size=30)}</span><h3>{s["nav"]}</h3><span class="svc-card__link">Learn more {icon("arrow-right",size=17)}</span></a>' for s in SERVICES[:3])}
  </div>
</div></section>
'''
    out += page_end()
    # 404 must be at root, not /404.html/index.html
    with open(os.path.join(ROOT,"404.html"),"w",encoding="utf-8") as f:
        f.write(out)

# ============================================================ ROOT FILES
def build_root_files():
    write_root("CNAME", "londonhvacpros.ca\n")
    write_root("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n")
    LLMS = f"""# {SITE_NAME}

> {SITE_NAME} is a licensed HVAC company in {CITY}, Ontario that specializes in installing high-efficiency furnaces, air conditioners, and heat pumps, with rebate guidance and right-sized system design. Phone: {PHONE_DISPLAY}.

## Pages
- [Home]({DOMAIN}/): High-efficiency HVAC installation in {CITY}, ON
- [Services]({DOMAIN}/services/): Furnace, AC, heat pump, ductless, fireplace, thermostat, and duct services
- [About]({DOMAIN}/about/): Who we are and how we work
- [Contact]({DOMAIN}/contact/): Free quotes and service requests

## Key services
- [Furnace Installation & Repair]({DOMAIN}/services/furnace-repair/)
- [AC Installation & Repair]({DOMAIN}/services/ac-repair/)
- [Heat Pump Installation]({DOMAIN}/services/heat-pump-repair-installation/)
- [Ductless Mini-Split Installation]({DOMAIN}/services/ductless-ac-installation/)
"""
    write_root("llms.txt", LLMS)
    write_root(".nojekyll", "")
    urls = ["/","/about/","/services/","/blog/","/contact/","/privacy-policy/"]
    urls += [f"/services/{s['slug']}/" for s in SERVICES]
    urls += [f"/blog/{p['slug']}/" for p in BLOG]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemap.org/schemas/sitemap/0.9">'.replace("sitemap.org","sitemaps.org")]
    for u in urls:
        pr = "1.0" if u=="/" else ("0.9" if u.startswith("/services") else "0.7")
        sm.append(f"  <url><loc>{DOMAIN}{u}</loc><changefreq>monthly</changefreq><priority>{pr}</priority></url>")
    sm.append("</urlset>")
    write_root("sitemap.xml", "\n".join(sm)+"\n")

# ============================================================ FAVICON
def build_favicon():
    os.makedirs(os.path.join(ROOT,"assets","img"), exist_ok=True)
    with open(os.path.join(ROOT,"assets","img","favicon.svg"),"w",encoding="utf-8") as f:
        f.write(LOGO_MARK.replace('class="brand__mark" ',''))

# ============================================================ RUN
def main():
    build_favicon()
    build_home()
    build_services_index()
    for slug,data in SVC.items():
        build_service(slug,data)
    build_about()
    build_contact()
    build_blog_index()
    build_blog_posts()
    build_privacy()
    build_404()
    build_root_files()
    print("✓ Site generated.")

if __name__ == "__main__":
    main()
