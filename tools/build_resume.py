from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    HRFlowable,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
)


ROOT = Path(__file__).resolve().parents[1]
OUTPUTS = [
    ROOT / "output" / "pdf" / "fredric-shernoff-game-producer-resume.pdf",
    ROOT / "resume" / "fredric-shernoff-resume.pdf",
]

NAVY = colors.HexColor("#102033")
INK = colors.HexColor("#1D2937")
MUTED = colors.HexColor("#52606D")
ACCENT = colors.HexColor("#C95E43")
PALE = colors.HexColor("#EEF3F5")
WHITE = colors.white


class ResumeDocTemplate(BaseDocTemplate):
    def __init__(self, filename: str):
        super().__init__(
            filename,
            pagesize=letter,
            leftMargin=0.62 * inch,
            rightMargin=0.62 * inch,
            topMargin=0.54 * inch,
            bottomMargin=0.48 * inch,
            title="Fredric Shernoff - Game Producer Resume",
            author="Fredric Shernoff",
            subject="Game production, product development, education, and Jewish community leadership",
        )
        frame = Frame(
            self.leftMargin,
            self.bottomMargin,
            self.width,
            self.height,
            id="resume",
            leftPadding=0,
            rightPadding=0,
            topPadding=0,
            bottomPadding=0,
        )
        self.addPageTemplates(PageTemplate(id="resume", frames=frame, onPage=self._decorate_page))

    def _decorate_page(self, canvas, doc):
        canvas.saveState()
        if doc.page == 1:
            canvas.setFillColor(NAVY)
            canvas.rect(0, letter[1] - 0.18 * inch, letter[0], 0.18 * inch, fill=1, stroke=0)
        else:
            canvas.setStrokeColor(PALE)
            canvas.setLineWidth(0.7)
            canvas.line(doc.leftMargin, letter[1] - 0.34 * inch, letter[0] - doc.rightMargin, letter[1] - 0.34 * inch)
            canvas.setFont("Helvetica-Bold", 8.4)
            canvas.setFillColor(NAVY)
            canvas.drawString(doc.leftMargin, letter[1] - 0.28 * inch, "FREDRIC SHERNOFF")
            canvas.setFont("Helvetica", 8.1)
            canvas.setFillColor(MUTED)
            page_label = f"GAME PRODUCER RESUME  |  {doc.page}"
            canvas.drawRightString(letter[0] - doc.rightMargin, letter[1] - 0.28 * inch, page_label)

        canvas.setFont("Helvetica", 7.8)
        canvas.setFillColor(MUTED)
        canvas.drawString(doc.leftMargin, 0.24 * inch, "fshernoff.github.io")
        canvas.drawRightString(letter[0] - doc.rightMargin, 0.24 * inch, "fshernoff@gmail.com  |  215-512-1255")
        canvas.restoreState()


styles = getSampleStyleSheet()
styles.add(
    ParagraphStyle(
        name="Name",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=25,
        leading=28,
        textColor=NAVY,
        alignment=TA_CENTER,
        spaceAfter=1,
    )
)
styles.add(
    ParagraphStyle(
        name="Headline",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=10.5,
        leading=13,
        textColor=ACCENT,
        alignment=TA_CENTER,
        spaceAfter=3,
    )
)
styles.add(
    ParagraphStyle(
        name="Contact",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=8.6,
        leading=11.5,
        textColor=MUTED,
        alignment=TA_CENTER,
        spaceAfter=8,
    )
)
styles.add(
    ParagraphStyle(
        name="Section",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=10.7,
        leading=13,
        textColor=NAVY,
        spaceBefore=7,
        spaceAfter=4,
        keepWithNext=True,
    )
)
styles.add(
    ParagraphStyle(
        name="Summary",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=9.35,
        leading=12.4,
        textColor=INK,
        spaceAfter=3,
    )
)
styles.add(
    ParagraphStyle(
        name="Strength",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=8.85,
        leading=11.5,
        textColor=INK,
        leftIndent=8,
        firstLineIndent=-8,
        spaceAfter=2.4,
    )
)
styles.add(
    ParagraphStyle(
        name="Role",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=9.5,
        leading=11.5,
        textColor=NAVY,
        spaceBefore=5.5,
        spaceAfter=1,
        keepWithNext=True,
    )
)
styles.add(
    ParagraphStyle(
        name="Org",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=8.6,
        leading=10.8,
        textColor=MUTED,
        spaceAfter=2.2,
        keepWithNext=True,
    )
)
styles.add(
    ParagraphStyle(
        name="ResumeBullet",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=8.7,
        leading=11.2,
        textColor=INK,
        leftIndent=13,
        firstLineIndent=-7,
        bulletIndent=0,
        spaceAfter=2.2,
    )
)
styles.add(
    ParagraphStyle(
        name="Compact",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=8.55,
        leading=10.9,
        textColor=INK,
        spaceAfter=2.2,
    )
)


def section(title: str):
    return [
        Spacer(1, 1),
        Paragraph(title.upper(), styles["Section"]),
        HRFlowable(width="100%", thickness=0.8, color=ACCENT, spaceBefore=0, spaceAfter=3.2),
    ]


def bullet(text: str):
    return Paragraph(f"-&nbsp;&nbsp;{text}", styles["ResumeBullet"])


def role(title: str, org: str, dates: str):
    return [
        Paragraph(title, styles["Role"]),
        Paragraph(f"{org}  |  {dates}", styles["Org"]),
    ]


def story():
    items = [
        Spacer(1, 1),
        Paragraph("Fredric Shernoff", styles["Name"]),
        Paragraph("GAME PRODUCER  |  PRODUCT DEVELOPER  |  EDUCATOR", styles["Headline"]),
        Paragraph(
            'Palm Beach Gardens, FL &nbsp;|&nbsp; 215-512-1255 &nbsp;|&nbsp; '
            '<a href="mailto:fshernoff@gmail.com" color="#52606D">fshernoff@gmail.com</a> &nbsp;|&nbsp; '
            '<a href="https://fshernoff.github.io" color="#C95E43"><u>fshernoff.github.io</u></a>',
            styles["Contact"],
        ),
    ]

    items += section("Professional Summary")
    items.append(
        Paragraph(
            "Game producer, product developer, and educator who turns creative, technical, and learning goals into shipped digital experiences. "
            "Independently designed and published a commercial Steam game; built classroom and school operations platforms; launched native mobile and streaming products; and led organizations, vendors, and multi-stakeholder work. "
            "Brings hands-on technical fluency, production discipline, classroom perspective, and deep Jewish education and community experience.",
            styles["Summary"],
        )
    )

    items += section("Production Strengths")
    for text in [
        "<b>Game and product production:</b> scope, roadmaps, milestones, prioritization, risk management, playtesting, QA, launch, and iteration",
        "<b>Creative direction:</b> gameplay loops, systems design, player experience, educational design, UI/UX, and constructive build feedback",
        "<b>Technical fluency:</b> Unity, C#, Godot, React, TypeScript, Firebase, Swift/SwiftUI, Android, APIs, Git, automated testing, and CI/CD",
        "<b>Leadership:</b> stakeholder translation, internal and external contributors, vendor coordination, documentation, operational systems, and community engagement",
        "<b>AI-enabled workflow:</b> rapid prototyping, research, evaluation, automation, asset exploration, testing support, and responsible classroom use",
    ]:
        items.append(Paragraph(f"<b>+</b>&nbsp;&nbsp;{text}", styles["Strength"]))

    items += section("Relevant Experience")
    items += role(
        "AI Teacher",
        "Jupiter Community High School, School District of Palm Beach County",
        "Current",
    )
    items += [
        bullet(
            "Develop and teach applied AI learning experiences that move students from responsible tool use and evaluation to project planning, creation, and reflection."
        ),
        bullet(
            "Translate fast-changing technology into clear, age-appropriate workflows; coach students through ambiguous problems, iterative feedback, and working deliverables."
        ),
        bullet(
            "Designed and built <b>Aegis</b>, a production-ready school operations platform with role-aware dashboards, public kiosks, real-time capacity controls, analytics, audit trails, and automated tests."
        ),
    ]

    items += role(
        "Independent Game Producer and Product Developer",
        "Independent Ventures / Whitemarsh Games",
        "2010 - Present",
    )
    items += [
        bullet(
            '<b>Scorched Legacy:</b> independently scoped, designed, developed, balanced, playtested, and published a commercial PC artillery roguelike on '
            '<a href="https://store.steampowered.com/app/4326140/Scorched_Legacy/" color="#C95E43"><u>Steam</u></a>; owned gameplay systems, UX, achievements, store materials, release, and iteration.'
        ),
        bullet(
            '<b>BizBattles:</b> created a <a href="https://businessbattles.web.app/teachers" color="#C95E43"><u>live-beta</u></a>, teacher-led multiplayer business simulation with team decisions, changing market conditions, real-time class management, and concept-focused debriefs.'
        ),
        bullet(
            '<b>Additional work:</b> released <a href="https://whitemarshgames.itch.io/datacenter-tycoon" color="#C95E43"><u>Data Center Tycoon</u></a> free on itch.io; developing the Unity narrative game <b>Divine Nuisance</b>; previously shipped MyFandom for iOS/Android and Draw Anything AI for iOS.'
        ),
    ]

    items.append(PageBreak())

    items += section("Professional Experience, Continued")
    items += role(
        "Chief Executive Officer and Lead iOS Developer",
        "Premier Streaming Network (Streaming Media Ventures, LLC)",
        "2022 - Present",
    )
    items += [
        bullet(
            "Led product and technical direction for a SwiftUI streaming platform from concept through delivery, coordinating business goals with content, design, engineering, and distribution needs."
        ),
        bullet(
            "Built core platform capabilities including adaptive video streaming, authentication, API integrations, and real-time chat; established modular architecture and repeatable release workflows."
        ),
        bullet(
            "Managed priorities, partnerships, quality, and iteration across a fast-moving product with multiple stakeholders and distribution requirements."
        ),
    ]

    items += role(
        "Co-Founder and Operations Manager",
        "Open Minds Academy | Wellington, FL",
        "2020 - 2022",
    )
    items += [
        bullet(
            "Built operating systems for a new educational institution, including enrollment, communications, program management, planning, and repeatable workflows for growth."
        ),
        bullet(
            "Balanced student, family, educator, and organizational needs while turning broad educational goals into clear processes and deliverables."
        ),
    ]

    items += role(
        "President and Broker",
        "Tri Star Commercial Real Estate | Warrington, PA",
        "2001 - 2022",
    )
    items += [
        bullet(
            "Led operations and digital transformation across a multi-stakeholder real estate business, including CRM implementation, vendor relationships, standardized procedures, and complex project execution."
        ),
        bullet(
            "Created scalable documentation and operating practices while managing competing priorities, deadlines, client relationships, and business risk."
        ),
    ]

    items += section("Jewish Education and Community Leadership")
    items += [
        Paragraph(
            "<b>Religious School Teacher and Curriculum Developer</b>  |  Temple Sinai, Dresher, PA (2000 - 2009)  |  Temple Beth Torah, Wellington, FL (2017 - 2018)",
            styles["Compact"],
        ),
        bullet(
            "Developed curriculum and taught K-7 learners; created technology-supported programs while building strong relationships with students, families, and community members."
        ),
        Paragraph(
            "<b>Additional leadership:</b> Temple Beth Torah cantor selection committee (2021), including stakeholder communication and selection-process coordination; communications chair for a local United Synagogue Youth branch; longtime participant in Jewish educational and communal life, including Camp Ramah in the Poconos.",
            styles["Compact"],
        ),
    ]

    items += section("Education and Credentials")
    items += [
        Paragraph("<b>MBA, Management</b>  |  Lehigh University College of Business  |  2008", styles["Compact"]),
        Paragraph("<b>BA, Psychology</b>  |  Temple University", styles["Compact"]),
        Paragraph("<b>Computer Science Certification</b>  |  Massachusetts Institute of Technology", styles["Compact"]),
        Paragraph(
            "<b>Secondary Diploma, Youth Leadership Certificate, and Jewish Educators Certificate</b>  |  Jewish Community High School of Gratz College",
            styles["Compact"],
        ),
    ]

    return items


def build():
    for output in OUTPUTS:
        output.parent.mkdir(parents=True, exist_ok=True)
        ResumeDocTemplate(str(output)).build(story())
        print(output)


if __name__ == "__main__":
    build()
