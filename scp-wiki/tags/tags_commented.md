

[[module CSS]]
#edit-page-form .buttons.alignleft::before {
  content: "Please make sure you understand the warning at the top of the page source before saving your edits!";
  display: block;
  margin-bottom: 1em;
  font-weight: bold;
  color: red;
}

#page-content ul > li {
  margin-top: 0.5em;
  line-height: 1.25em;
}

#page-content ul > li li {
  margin-top: 0.25em;
  list-style: circle;
}
[[/module]]

> This page has a comprehensive list of tags available on the wiki.  For help with actually deciding which tags to use, please refer to the [[[tech-hub-tag | tag guide]]].

When choosing tags for an article, keep in mind that you want to keep the list as short as possible; the goal should be to choose tags that are already being used, rather than create a new one. If staff should determine that a new tag is necessary, they can always retroactively tag articles as necessary. If you would like to suggest a new tag, please do so in the [https://scp-wiki.wikidot.com/forum/c-51015/proposals-and-policy stickied tag suggestion thread].

//For Wiki staff: to update this page, see [[[tag list manifest|]]]//

[[tabview]]

[[tab Top Level]]
++ Top Level

All pages on the wiki should have exactly one top-level tag that determines what kind of page it is.

+++ Fictional works

The following tags are for pages that contain fiction.

* **[https://scp-wiki.wikidot.com/system:page-tags/tag/scp scp]** -- All SCP articles from the main blocks, [https://scp-wiki.wikidot.com/scp-001 001 proposals], [https://scp-wiki.wikidot.com/joke-scps jokes] (-J), [https://scp-wiki.wikidot.com/archived-scps archives] (-ARC), and [https://scp-wiki.wikidot.com/scp-ex explained] (-EX) articles should be tagged with //scp//.
 * //Requires any of category 'object-class'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/goi-format goi-format]** -- The page has been written up from the perspective of a specific Group of Interest, and conforms to the format(s) laid out in that GoI's hub page. GoI Formats should also be tagged with the tag of their GoI, as well as the underscore tag for the GoI format.
 * //Requires any of category 'goi-format'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/tale tale]** -- Any fiction that is set in the SCP universe but is not an SCP, GoI Format, site page or supplement.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/supplement supplement]** -- //supplement// pages are defined as pages which require context from their parent page to understand. These pages should also have their parent page set to their originating article in order to maintain relevance and automatically create breadcrumb navigation. A page should only be tagged as //supplement// if they were created by the original author of the page, or with the original author's permission. Documents that are tributes or parodies should be tagged as //tale// instead, even if they are in the format of a log or transcript.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/site site]** -- //site// pages are hub pages that document specific Foundation facilities, and provide information such as the objects stored at the site, site history, assigned personnel, etc. A page tagged //site// that is also a hub page e.g. for SCPs contained within that site should also be tagged //hub//.

+++ Information pages

These pages contain information about the site or the writing process.

* **[https://scp-wiki.wikidot.com/system:page-tags/tag/guide guide]** -- These pages are writing guides, helpful hints, or other pages intended to assist site users. Guides are only tagged by staff, or with staff permission. See also //essay//.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/essay essay]** -- //essay// pages contain useful information on specific topics that may be helpful to authors writing related articles, but are different from a //guide// in that essays are subjective and reflect the author's personal opinion.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/news news]** -- //news// pages contain news about the SCP Foundation in the broadest sense of the word, ranging from new artwork by fans to recently posted successful articles and everything in between. May also be used for formal announcements by staff (in as far as those aren't done on the main page or in the forum).
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/resource resource]** -- //resource// pages list various aspects of the SCP canon, optionally also adding information regarding them.

+++ User pages

Pages for site members to showcase their body of work.

* **[https://scp-wiki.wikidot.com/system:page-tags/tag/author author]** -- This tag should be used for author profile pages. There should only be a single author profile page for each qualifying site member.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/artist artist]** -- This tag should, similarly, be used for artist profile pages. If a site member wants more than one artist profile page, they must get staff permission first.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/artwork artwork]** -- //artwork// pages host Foundation-related artwork created by community members, whether as individual pieces or collections.

+++ Import pages

These pages are designed to be imported onto other pages.

* **[https://scp-wiki.wikidot.com/system:page-tags/tag/component component]** -- A page that is designed to be imported onto other pages via the {{@@[[include]]@@}} syntax in order to add new design, style or functionality.
 * //Conflicts with 'component-backend'//
 * //Superseded by 'theme', and 'more-by'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/component-backend component-backend]** -- An 'internal template' page that is designed only to be imported into other //component// or //component-backend// pages, but not used directly by authors.
 * //Conflicts with 'component'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/theme theme]** -- Theme pages are templates that modify the general look and feel of a page.
 * //Supersedes 'component'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/fragment fragment]** -- A page that is designed to be imported onto a single page, and contains content for that page only. They should be parented to that page. Pages of this type should be in the {{fragment:}} category and are exempt from deletion as long as their parent exists on the wiki. If they are orphaned or their parent is deleted, they are eligible for summary deletion.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/more-by more-by]** -- A page that lists works by a single author, designed to be imported onto that author's published works on the Wiki. They should be parented to that author's author page, if they have one. Pages of this type should be in the {{more-by:}} category and are exempt from voting. EN recommends that other branches do not translate these pages.
 * //Supersedes 'component'//

+++ Internal pages

Pages created for internal use.

* **[https://scp-wiki.wikidot.com/system:page-tags/tag/forum forum]** -- //forum// pages are those required for internal functioning of Wikidot's forum system. They should only be created by staff.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/splash splash]** -- //splash// pages are used as 'cover pages' for certain articles. (see: [https://scp-wiki.wikidot.com/SCP-902 SCP-902] >> [https://scp-wiki.wikidot.com/902-warning SCP-902 Warning].

+++ Other pages

* **[https://scp-wiki.wikidot.com/system:page-tags/tag/admin admin]** -- //admin// pages, as the name suggest, have some sort of official significance. Typically, they represent pages which are required to exist by Wikidot for some form of site functionality. They should only be created by staff.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/hub hub]** -- //hub// pages are pages with a large number of links to related pages. All of the SCP series pages are //hub// pages, as are the tale index and various other pages around the site. As it is a major page tag, hubs may not have other top-level tags (e.g. //scp// or //tale//), with the exception of //contest// pages. Tale hubs should additionally be tagged with the //_tale-hub// page.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/workbench workbench]** -- Workbenches are pages created by mods and admins to allow them to monitor certain pages using Wikidot's modules. While you're free to use those same monitors on your //author// page, **please do not create any workbench pages unless you're a moderator or admin**, or have received explicit permission from them to do so.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/sandbox sandbox]** -- In the very distant past, sandboxes on the main site were allowed. This was before the number of members became so big that the amount of sandboxes would create a total mess on the wiki. **Please note that personal sandboxes are no longer allowed on the main site.** The SCP Sandbox wiki at https://scp-sandbox-3.wikidot.com/ should be used for article drafts. Only staff may authorize new sandboxes on the site.

[[/tab]]

[[tab Major Page Tags]]
++ Major Page Tags

Miscellaneous major page tags that are not top-level tags.

* **[https://scp-wiki.wikidot.com/system:page-tags/tag/joke joke]** -- Pages which are considered 'jokes' or explicitly 'out-of-universe'. Joke pages can be parodies of any page type, and should also be tagged as such a page usually would. See [https://scp-wiki.wikidot.com/joke-scps Joke SCPs] for more information on Joke pages.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/poetry poetry]** -- Applicable if the page consists significantly of a form of poetry, with elements such as meter and rhyme.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/archived archived]** -- Pages which have been archived due to having been superseded, obsoleted, or inactivity. These pages should also be moved to the {{archived:}} category so they retain the 'archived page' notice and are locked from edits. See [https://scp-wiki.wikidot.com/archived-scps Archived Pages] for more information on archival.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/explained explained]** -- [https://scp-wiki.wikidot.com/scp-ex Explained] SCPs are a special sub-type of //scp//, and should be added to -EX articles as appropriate. Explained articles should also be tagged with their standard object class tag, or //esoteric-class// if the format does not specify a standard object class.
 * //Requires 'scp'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/decommissioned decommissioned]** -- Indicates the SCP has been destroyed in-universe upon article deletion out-of-universe. This is no longer in practice, see [https://scp-wiki.wikidot.com/archived:decommissioned-scps Decommissioned SCPs] for more details.
 * //Requires 'scp'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/001-proposal 001-proposal]** -- This is the tag for the articles proposing a possible [https://scp-wiki.wikidot.com/scp-001 SCP-001] object. SCPs tagged with this tag should also be tagged with their standard object class tag, or //esoteric-class// if applicable.
 * //Often used with 'scp'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/creepypasta creepypasta]** -- //creepypasta// are fiction that are unrelated to the SCP Foundation, and usually take the form of urban myths or campfire stories. Creepypasta is only appropriate for the SCP website if it's an original //creepypasta// by the posting author; we are not a repository for unattributed //creepypasta//.
 * //Requires 'tale'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/collaboration collaboration]** -- //collaboration// pages are those pages that are or were open to additions from any member, with the caveat that staff and the original author reserve the right to modify or delete entries found to be subpar, or close entries entirely.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/co-authored co-authored]** -- //co-authored// pages are the result of two or more authors working together, but are not open to additions from other members (unless otherwise specified).
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/contest contest]** -- //contest// pages are pages created for the purpose of community contests. This should be used in conjunction with //hub// in the case of entry listings, and should not be used on the entries themselves. These contests are only created by staff or with staff permission.
 * //Requires 'hub'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/required required]** -- //required// pages are guides that are part of the required reading for joining the SCP Wiki.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/redirect redirect]** -- //redirect// pages are those which redirect the user to a different page. They should only be created by staff or with explicit staff permission, excepting [https://scp-wiki.wikidot.com/adult-page-guide adult pages].
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_tale-hub _tale-hub]** -- Utilized in conjunction with the //hub// tag to designate that this hub represents a series that consists mostly or entirely of //tale// articles.
 * //Requires 'hub'//

+++ Supplement pages

Tags that describe the content of a //supplement// page.

* **[https://scp-wiki.wikidot.com/system:page-tags/tag/experiment experiment]** -- This supplement contains primarily experiment logs (see: [https://scp-wiki.wikidot.com/SCP-914 SCP-914] >> [https://scp-wiki.wikidot.com/Experiment-Log-914 Experiment Log 914]). This tag **should not** be used on //scp// pages, even if they have extensive experiment logs.
 * //Requires 'supplement'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/exploration exploration]** -- This supplement contains primarily exploration logs. This tag **should not** be used on //scp// pages, even if they have extensive exploration logs.
 * //Requires 'supplement'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/incident incident]** -- This supplement contains primarily incident logs or transcripts (see: [https://scp-wiki.wikidot.com/SCP-555 SCP-555] >> [https://scp-wiki.wikidot.com/Incident-Log-555-1 Incident Log 555-1]). This tag **should not** be used on //scp// pages, even if they have extensive incident logs.
 * //Requires 'supplement'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/interview interview]** -- This supplement contains primarily interview transcripts (see: [https://scp-wiki.wikidot.com/SCP-277 SCP-277] >> [https://scp-wiki.wikidot.com/277interview Interview 277-A]). This tag **should not** be used on //scp// pages, even if they have extensive interview transcripts.
 * //Requires 'supplement'//

[[/tab]]

[[tab Object Classes]]
++ Object Classes

All SCP articles tagged as scp should also be tagged with the appropriate tag for their object class or esoteric-class if it does not have one, if its object class cannot be determined from the article's contents, or if it has a non-standard object class. Legacy articles that are dual-classed (such as safe/euclid) are tagged with both of their constituent classes; however, as this is no longer allowed, it is only for posterity until all such articles are updated or deleted.

[[div class="blockquote"]]
The following applies to all tags in this category:

* Requires 'scp'

[[/div]]

* **[https://scp-wiki.wikidot.com/system:page-tags/tag/safe safe]** -- SCP is Safe.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/euclid euclid]** -- SCP is Euclid.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/keter keter]** -- SCP is Keter.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/thaumiel thaumiel]** -- SCP is Thaumiel.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/apollyon apollyon]** -- SCP is Apollyon.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/archon archon]** -- SCP is Archon.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/neutralized neutralized]** -- SCP is Neutralized.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/pending pending]** -- SCP is pending classification.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/esoteric-class esoteric-class]** -- SCP has an object class other than one of the above.

[[/tab]]

[[tab SCP Attributes]]
++ SCP Attributes

This list is intended as a guide to attribute tags, or secondary tags on SCP articles. When choosing tags for an article, keep in mind that you want to keep the list as short as possible; the goal should be to choose tags that are already being used, rather than create a new one. If staff should determine that a new tag is necessary, they can always retroactively tag articles as necessary. If you would like to suggest a new tag, please do so in the discussion thread for this page.

The following tags are SCP Article attribute tags, and should only be used on SCP pages, not tales.

[[div class="blockquote"]]
The following applies to all tags in this category:

* Requires 'scp'

[[/div]]

* **[https://scp-wiki.wikidot.com/system:page-tags/tag/acoustic acoustic]** -- SCP is composed of, affects, generates, or is propagated by sound waves.
 * //Often used with 'vibration'//
 * //Avoid using with 'auditory'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/adaptive adaptive]** -- SCP adapts to stimuli in an anomalous manner.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/addictive addictive]** -- SCP causes desire or addictive behavior in affected subjects.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/airborne airborne]** -- SCP lives in, moves through, or spreads through the air.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/alive alive]** -- SCP is alive, meaning it exhibits the biological traits of metabolism, reaction, and reproduction. See the Tag [https://05command.wikidot.com/tech-hub-tag FAQ] for more information.
 * //Conflicts with 'autonomous'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/amorphous amorphous]** -- SCP lacks a set form or shape, constantly changes shape, or has a poorly-defined shape e.g. a blob.
 * //Conflicts with 'metamorphic'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/animal animal]** -- SCP is or exhibits traits of animal life.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/antimemetic antimemetic]** -- SCP is or involves the use of (an) antimeme(s) to suppress knowledge and/or understanding of an idea or concept, including itself.
 * //Avoid using with 'memetic'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/apian apian]** -- SCP is or exhibits traits of apian or bee-like animals.
 * //Often used with 'animal', and 'insect'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/appliance appliance]** -- SCP is or resembles a household or domestic appliance.
 * //Often used with 'electrical', and 'electronic'//
 * //Supersedes 'artifact'//
 * //Superseded by 'computer'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/aquatic aquatic]** -- SCP lives in, moves through or spreads through water.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/arachnid arachnid]** -- SCP is or exhibits traits of arachnid or spider-like animals.
 * //Often used with 'animal'//
 * //Conflicts with 'insect'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/arboreal arboreal]** -- SCP is or exhibits traits of arboreal or tree-like plants.
 * //Often used with 'plant'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/arthropod arthropod]** -- SCP is or exhibits traits of arthropods or animals with exoskeletons, segmented bodies, and jointed appendages.
 * //Supersedes 'invertebrate'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/artistic artistic]** -- SCP is a work of art, exhibits artistic properties, or has artistic significance.
 * //Superseded by 'musical', 'sculpture', and 'statue'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/artifact artifact]** -- SCP is or was originally created by humans.
 * //Superseded by 'appliance', 'clothing', 'computer', 'container', 'jewelry', 'media', 'timepiece', 'tool', 'toy', 'vehicle', and 'weapon'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/auditory auditory]** -- SCP is triggered by, activated by, or affects the sense of hearing.
 * //Avoid using with 'acoustic'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/automaton automaton]** -- SCP is a device or construct designed to operate on its own. Should be applied to anything that can be described as a 'robot'.
 * //Supersedes 'mechanical'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/autonomous autonomous]** -- SCP activates/operates on its own in an anomalous fashion. Only applicable to objects that normally do not activate on their own.
 * //Conflicts with 'alive'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/avian avian]** -- SCP is or exhibits traits of avian or bird-like animals.
 * //Often used with 'animal'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/bacteria bacteria]** -- SCP is, resembles, or exhibits traits of a bacterial life-form.
 * //Avoid using with 'contagion'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/bibliothetic bibliothetic]** -- SCP is, or is otherwise related to or affects libraries, defined as a room or building containing books for people to read or borrow.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/biohazard biohazard]** -- SCP poses a hazard to humans or the environment as a result of biological function, or is a biological hazard.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/biological biological]** -- SCP exhibits biological traits. Please see the [https://05command.wikidot.com/tech-hub-tag FAQ] for more details.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/bovine bovine]** -- SCP is or exhibits traits of bovine or cattle-like animals.
 * //Often used with 'animal'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/building building]** -- SCP is, is a part of, or otherwise is related to or affects a building, defined as a structure intended for human occupation.
 * //Supersedes 'structure'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/cadaver cadaver]** -- SCP is, affects, or is related to corpses, carcasses, or any dead organic matter.
 * //Often used with 'reanimation', and 'skeletal'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/canine canine]** -- SCP is or exhibits traits of canine or dog-like animals.
 * //Often used with 'animal'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/carnivorous carnivorous]** -- SCP is or exhibits traits of carnivorous animals.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/cervine cervine]** -- SCP is or exhibits traits of cervine or deer-like animals. Also includes elk and moose.
 * //Often used with 'animal'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/cephalopodic cephalopodic]** -- SCP is or exhibits traits of cephalopods or animals including the cuttlefish, octopus, and squid.
 * //Often used with 'animal'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/cetacean cetacean]** -- SCP is or exhibits traits of cetacean or whale-like animal.
 * //Often used with 'animal'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/chemical chemical]** -- SCP is an anomalous chemical compound or produces chemical compounds in an anomalous way.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/city city]** -- SCP is a city, town, or other settlement intended for human occupation. Should only be used if a significant portion of the city is considered anomalous.
 * //Supersedes 'location'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/clay clay]** -- SCP is primarily or significantly composed of clay.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/clockwork clockwork]** -- SCP operates primarily via clockworks, defined as mechanical devices constructed primarily using toothed wheels and/or powered by a mainspring.
 * //Supersedes 'mechanical'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/clothing clothing]** -- SCP is an artifact primarily intended to be worn for protection or comfort, including armor and protective helmets.
 * //Conflicts with 'jewelry'//
 * //Supersedes 'artifact'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/cognitohazard cognitohazard]** -- SCP is hazardous to subjects when recorded by any of the traditional 5 senses.
 * //Often used with 'auditory', 'gustatory', 'olfactory', 'tactile', and 'visual'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/compulsion compulsion]** -- SCP induces compulsive behavior in subjects or otherwise causes subjects to do things they normally would not. See Tag [https://05command.wikidot.com/tech-hub-tag FAQ] for extended clarifications.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/computer computer]** -- SCP is a computational device or affects computational devices.
 * //Often used with 'electronic', and 'mechanical'//
 * //Supersedes 'artifact', and 'appliance'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/concept concept]** -- SCP is or affects a purely non-physical concept. Should not be used in conjunction with tags describing physical qualities.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/contagion contagion]** -- SCP is a contagious agent or exhibits contagious spread.
 * //Avoid using with 'bacteria'//
 * //Superseded by 'memetic', and 'virus'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/container container]** -- SCP is meant to hold or otherwise contain other material or objects, including decorative vases and other similar objects.
 * //Supersedes 'artifact'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/corporate corporate]** -- SCP affects the operations of a business or corporation.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/corrosive corrosive]** -- SCP exhibits corrosive properties.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/currency currency]** -- SCP is, is related to, affects, or is activated by money or other objects primarily intended to be used as a medium of exchange.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/crystalline crystalline]** -- SCP is or exhibits traits of crystals.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/cube cube]** -- SCP is cubical. Should only be used where the entire SCP is cubical or composed of cubes, rather than SCPs in which only one or more components are cubical.
 * //Supersedes 'polyhedral'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/dental dental]** -- SCP is or deals with teeth or the practice of dentistry.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/dinosaurian dinosaurian]** -- SCP is or relates to a non-avian dinosaur.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/document document]** -- SCP is a textual document of some sort. Includes books.
 * //Supersedes 'inscribed'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/ectoentropic ectoentropic]** -- SCP violates the first and/or second law of [https://en.wikipedia.org/wiki/Thermodynamics thermodynamics] by generating matter and/or energy in a fashion that directly violates entropy. Applies to anything that produces energy or matter in an unexplained way.
 * //Avoid using with 'extradimensional', and 'physics'//
 * //Superseded by 'ontokinetic'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/electrical electrical]** -- SCP generates, stores, or uses electric energy.
 * //Avoid using with 'physics'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/electromagnetic electromagnetic]** -- SCP generates, stores, or uses electromagnetic energy or fields.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/electronic electronic]** -- SCP is or resembles an electronic device.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/empathic empathic]** -- SCP is capable of reading or conveying emotion, feelings, or sensations.
 * //Often used with 'telepathic'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/engraved engraved]** -- SCP is or has carvings and/or engravings.
 * //Supersedes 'inscribed'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/entropic entropic]** -- SCP is, exhibits traits of, or is related to entropy or entropic decay.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/equine equine]** -- SCP is or exhibits traits of equine or horse-like animals.
 * //Often used with 'animal'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/exchange exchange]** -- SCP involves or is triggered by some form of exchange of physical or intangible goods, including but not limited to bartering and monetary trade.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/extradimensional extradimensional]** -- SCP is of extradimensional origin, moves or propagates extradimensionally, and/or enables extradimensional travel.
 * //Avoid using with 'ectoentropic'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/extraterrestrial extraterrestrial]** -- SCP originates or is found in outer space and/or enables or exhibits extraterrestrial travel.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/extremity extremity]** -- SCP is or affects specific extremities, regardless of species.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/feline feline]** -- SCP is or is related to feline or cat-like animals.
 * //Often used with 'animal'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/fire fire]** -- SCP is composed of fire, is related to fire, or enables the process of combustion.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/food food]** -- SCP is primarily intended to be an edible object or substance.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/foundation-made foundation-made]** -- SCP was created, intentionally or otherwise, by the SCP Foundation itself. Note that only the objects whose creation resulted directly from specific actions of the Foundation are applicable. This excludes phenomena which formed spontaneously at a Foundation site due to the area's routine exposure to a large number of contained anomalies.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/fungus fungus]** -- SCP is or exhibits traits of fungal life-forms.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/furniture furniture]** -- SCP is or resembles a piece of furniture.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/future future]** -- SCP is from the future or was otherwise temporally displaced from a later time frame into an earlier one.
 * //Often used with 'temporal'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/game game]** -- SCP is, is used in, is activated by, or is otherwise related to one or more games, defined as a method of play or a sport -- especially a competitive one -- that can be won or lost by skill, strength, or luck.
 * //Often used with 'sport'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/gaseous gaseous]** -- SCP is or generates a gas.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/genetic genetic]** -- SCP is related to or functions primarily via genetic encoding and decoding.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/geological geological]** -- SCP is or affects natural geological formations (such as caves, cliffs, mountains, valleys, or volcanoes) or significant geological events (such as earthquakes, landslides, or sinkholes).
 * //Superseded by 'planet'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/glass glass]** -- SCP is primarily or significantly composed of glass.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/gravity gravity]** -- SCP affects or is significantly affected by gravitational force.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/gustatory gustatory]** -- SCP is triggered by, activated by, or affects the sense of taste.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/hallucination hallucination]** -- SCP induces hallucinations in subjects or is a hallucination.
 * //Often used with 'auditory', and 'visual'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/historical historical]** -- SCP affects or is prominent in historical events or has historical significance.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/hive-mind hive-mind]** -- SCP exhibits traits of an external hive-mind.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/hostile hostile]** -- SCP exhibits directed hostility towards personnel or subjects above and beyond that of instinctual or predatory behavior.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/humanoid humanoid]** -- SCP is humanoid or exhibits traits of humanoids.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/immobile immobile]** -- SCP cannot be moved via any means known by the Foundation.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/indestructible indestructible]** -- SCP cannot be destroyed via any means known by the Foundation.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/infohazard infohazard]** -- SCP has an effect that is triggered when it is described or referred to. See Tag [https://05command.wikidot.com/tech-hub-tag FAQ] for extended clarifications.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/insect insect]** -- SCP is or is related to insects. (This **does not** includes spiders, which should be tagged as //arachnid//).
 * //Often used with 'animal'//
 * //Conflicts with 'arachnid'//
 * //Supersedes 'invertebrate'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/inscribed inscribed]** -- SCP has inscriptions on it, usually in the form of words or numbers.
 * //Superseded by 'document', and 'engraved'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/inscription inscription]** -- SCP is an inscription, meaning it takes the form of written or carved words or numbers.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/instrument instrument]** -- SCP is an instrument or a tool intended for either delicate, scientific, or measuring work.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/intangible intangible]** -- SCP is intangible in a manner that precludes definition as a gas.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/invertebrate invertebrate]** -- SCP exhibits traits of invertebrates or animals lacking spinal columns.
 * //Superseded by 'arthropod', and 'insect'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/jewelry jewelry]** -- SCP is an object primarily intended to be worn in a decorative manner.
 * //Conflicts with 'clothing'//
 * //Supersedes 'artifact'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/k-class-scenario k-class-scenario]** -- SCP is involved in or capable of instigating one or more K-Class End of the World scenarios. Should only be used in articles that specifically name a type of K-Class scenario.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/key key]** -- SCP is a standard key or otherwise intended to unlock one or more devices or containers.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/knowledge knowledge]** -- SCP absorbs, stores, generates, grants, or possesses knowledge that is anomalous, or through an anomalous process. SCPs capable of accurate predictions should be tagged //predictive// instead.
 * //Superseded by 'predictive'//
 * //Compare with 'telepathic'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/language language]** -- SCP imparts, exhibits, or is an anomalous language.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/lepidopteran lepidopteran]** -- SCP is or exhibits traits of lepidopteran or butterfly-, moth-, or skipper-like animals.
 * //Often used with 'animal', and 'insect'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/leporine leporine]** -- SCP is or exhibits traits of leporine or rabbit- or hare-like animals.
 * //Often used with 'animal'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/light light]** -- SCP is triggered, activated, or propagated by or otherwise related to the presence or absence of visible light.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/liquid liquid]** -- SCP is or generates a liquid.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/location location]** -- SCP is a unique geographical location.
 * //Superseded by 'city'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/loop loop]** -- SCP exhibits or is engaged in a repeating loop of activity.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/magnetic magnetic]** -- SCP is magnetic or exhibits traits of magnetic charge and/or attraction.
 * //Avoid using with 'physics'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/map map]** -- SCP is a map, has a map, or otherwise exhibits visual representations in the manner of a map.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/mathematical mathematical]** -- SCP is or affects a number, number system, mathematical equation, or otherwise has mathematical significance.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/mechanical mechanical]** -- SCP operates primarily in a mechanical manner or is a mechanical device.
 * //Superseded by 'automaton', and 'clockwork'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/media media]** -- SCP is or is contained on, one or more items of fixed or removable analog or digital media, such as a tape, record, disc, or drive.
 * //Supersedes 'artifact'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/medical medical]** -- SCP is used or intended for use as a medical device or otherwise has medical significance outside of pathology.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/memetic memetic]** -- SCP is a memetic agent or exhibits traits of [https://scp-wiki.wikidot.com/Understanding-Memetics memetic propagation]. See Tag [https://05command.wikidot.com/tech-hub-tag FAQ] for extended clarifications.
 * //Often used with 'cognitohazard'//
 * //Avoid using with 'antimemetic'//
 * //Supersedes 'contagion'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/memory-affecting memory-affecting]** -- SCP imparts, changes, or removes memories in sentient beings such as human subjects.
 * //Compare with 'mind-affecting'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/meta meta]** -- SCP affects or is affected by its documentation or requires containment procedures regarding the way it is documented. See Tag [https://05command.wikidot.com/tech-hub-tag FAQ] for extended clarifications.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/metallic metallic]** -- SCP is a metal or is completely or significantly composed of metal or metallic substances.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/metamorphic metamorphic]** -- SCP changes its form or shape, often to mimic the form or shape of other objects or entities. Often used to describe shapeshifters or mimics.
 * //Conflicts with 'amorphous'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/meteorological meteorological]** -- SCP is, affects, or is affected by significant weather elements.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/microscopic microscopic]** -- SCP is too small to be seen or otherwise meaningfully observed by the naked eye.
 * //Compare with 'miniature'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/military military]** -- SCP is military equipment, part or member of a military unit, or otherwise has military significance.
 * //Compare with 'weapon'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/mimetic mimetic]** -- SCP exhibits anomalous mimicry.
 * //Often used with 'auditory', 'gustatory', 'olfactory', 'tactile', and 'visual'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/mind-affecting mind-affecting]** -- SCP affects the thinking of subjects, which can include behavior and overall intelligence. See Tag [https://05command.wikidot.com/tech-hub-tag FAQ] for extended clarifications.
 * //Compare with 'memory-affecting'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/miniature miniature]** -- SCP is much smaller than objects it resembles.
 * //Compare with 'microscopic'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/mobile mobile]** -- SCP is capable of movement by anomalous means. Generally only applies to objects or entities that are normally incapable of movement.
 * //Avoid using with 'teleportation'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/moon moon]** -- SCP is, is related to, or affects a natural satellite or moon, which may or may not be our moon.
 * //Often used with 'satellite'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/murine murine]** -- SCP is or exhibits traits of murine, or mouse-like or rat-like animals.
 * //Often used with 'animal'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/musical musical]** -- SCP is, generates, or is generated by musical compositions.
 * //Supersedes 'artistic'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/narrative narrative]** -- SCP is, is related to, or propagates via narrative information or documents.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/neurological neurological]** -- SCP directly or indirectly affects the neurological system of subjects. Only applicable in situations where objective neurological changes are confirmed, as opposed to a simple change of behavior in the subject.
 * //Often used with 'mind-affecting', and 'memory-affecting'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/nocturnal nocturnal]** -- SCP is triggered by, activated by, or otherwise is only significantly active at night.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/observational observational]** -- SCP has properties that are triggered or suppressed when directly or indirectly observed. These properties may or may not also be //cognitohazards//.
 * //Often used with 'cognitohazard'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/ocular ocular]** -- SCP resembles, is related to, or affects eyes.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/olfactory olfactory]** -- SCP exhibits anomalous scent, is propagated through smell, or affects the sense of smelling.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/omnivorous omnivorous]** -- SCP exhibits omnivorous traits.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/online online]** -- SCP is available on, utilizes, or is dependent on a connection to the internet.
 * //Often used with 'computer', and 'electronic'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/ontokinetic ontokinetic]** -- SCP is capable of manipulating reality (aka 'reality-bending') through anomalous means.
 * //Supersedes 'ectoentropic'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/ophidian ophidian]** -- SCP is or exhibits traits of ophidian, or snake-like animals.
 * //Often used with 'animal'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/organic organic]** -- SCP exhibits organic traits or composition. See Tag [https://05command.wikidot.com/tech-hub-tag FAQ] for extended clarifications.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/paradox paradox]** -- SCP generates, exhibits, or is involved in paradoxical events or situations.
 * //Compare with 'temporal'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/parasitic parasitic]** -- SCP exhibits traits of parasitic or parasitoid organisms.
 * //Avoid using with 'reproductive'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/performance performance]** -- SCP is or is used in a performance art, such as a dance or play.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/physics physics]** -- SCP affects or violates particular physical laws.
 * //Avoid using with 'ectoentropic', 'electrical', and 'magnetic'//
 * //Superseded by 'thermodynamic'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/photographic photographic]** -- SCP is or deals with photography or features a photograph as part of the primary anomaly.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/piscine piscine]** -- SCP is or exhibits traits of piscine or fish-like animals.
 * //Often used with 'animal'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/plant plant]** -- SCP is a plant or exhibits plant-like traits.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/planet planet]** -- SCP is, resembles, or affects a planet, which may or may not be our planet.
 * //Supersedes 'geological'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/polyhedral polyhedral]** -- SCP is a polyhedron: a three-dimensional shape with flat faces and straight edges.
 * //Superseded by 'cube'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/portal portal]** -- SCP is an opening or doorway that exhibits inconsistent connectivity.
 * //Often used with 'extradimensional', and 'spacetime'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/predatory predatory]** -- SCP exhibits predatory behavior.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/predictive predictive]** -- SCP is capable of imparting information or acting in a predictive manner.
 * //Supersedes 'knowledge'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/probability probability]** -- SCP alters or manipulates the probability of certain events or outcomes.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/radioactive radioactive]** -- SCP emits radiation or affects radioactivity.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/ranine ranine]** -- SCP is or exhibits traits of ranine or frog-like animals.
 * //Often used with 'animal'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/reanimation reanimation]** -- SCP has been restored or restores others, either whole or in part, to life from a clinically dead state.
 * //Often used with 'cadaver'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/recording recording]** -- SCP is or contains an audio and/or visual recording.
 * //Often used with 'media'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/religious religious]** -- SCP is associated with or otherwise has significance to one or more organized religions.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/reproductive reproductive]** -- SCP anomalously affects or interferes with the normal biological reproductive processes of an organism (which may include humans), or has anomalous biological reproductive methods other than that covered by //parasitic// or //self-replicating//.
 * //Avoid using with 'parasitic', and 'self-replicating'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/reptilian reptilian]** -- SCP is or exhibits traits of reptilian or reptile-like animals.
 * //Often used with 'animal'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/ritual ritual]** -- SCP is or is triggered or activated through ritualistic behavior.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/sapient sapient]** -- SCP exhibits sapient traits, such as the ability to grasp philosophical concepts.
 * //Often used with 'sentient'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/satellite satellite]** -- SCP is a natural or artificial satellite orbiting a celestial body.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/sciurine sciurine]** -- SCP is or exhibits traits of sciurine or squirrel-like animals.
 * //Often used with 'animal'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/sculpture sculpture]** -- SCP is a three-dimensional piece of artwork. To be considered a //sculpture//, the object in question must have been formed, carved, or molded.
 * //Supersedes 'artistic'//
 * //Superseded by 'statue'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/selachian selachian]** -- SCP is or exhibits traits of selacian or shark-like animals. Also includes rays and skates.
 * //Requires 'piscine'//
 * //Often used with 'animal'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/self-repairing self-repairing]** -- SCP exhibits an anomalous ability restore or repair itself to functional condition.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/self-replicating self-replicating]** -- SCP exhibits an anomalous ability to replicate other than via biological reproduction.
 * //Avoid using with 'reproductive'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/sensory sensory]** -- SCP affects sensory perception.
 * //Often used with 'auditory', 'gustatory', 'olfactory', 'tactile', and 'visual'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/sexual sexual]** -- SCP includes or affects sexual organs, sexual activities, or concepts related to sex. Does not imply that the work is intended for adult audiences only.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/sentient sentient]** -- SCP exhibits sentient traits, such as self-awareness and cognitive deduction.
 * //Often used with 'sapient'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/shadow shadow]** -- SCP is triggered, activated, or otherwise significantly affected by shadows cast by subjects.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/simian simian]** -- SCP is or exhibits traits of simian, or ape-like animals.
 * //Often used with 'animal'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/skeletal skeletal]** -- SCP is, is a component of, or affects the skeletal tissue of an organism. A skeleton is the structural support tissue of a multi-celled organism, and includes both bones and cartilage.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/sleep sleep]** -- SCP is related to sleep.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/spacetime spacetime]** -- SCP warps space-time or affects or violates laws of space-time.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/species species]** -- SCP describes an entire species, rather than one or more individuals.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/sphere sphere]** -- SCP is spherical.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/sport sport]** -- SCP is, is used in, is activated by, or is otherwise related to one or more sports, defined as an activity involving physical exertion and skill in which one or more individuals compete against other individuals or teams. Sports should also be tagged with //game//. Equipment or gear specifically or exclusively used in sporting events should also be tagged with //clothing// or //tool//, as appropriate.
 * //Compare with 'game', 'clothing', and 'tool'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/statue statue]** -- SCP is or was a statue. A statue is defined as a free-standing, full-body //sculpture// of a person or animal.
 * //Supersedes 'artistic', and 'sculpture'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/stone stone]** -- SCP is composed primarily of stone (meaning concreted earthy or mineral matter) or rock.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/structure structure]** -- SCP is an artificial or natural structure; if it is intended for human occupation, it should be tagged //building// instead.
 * //Superseded by 'building'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/subterranean subterranean]** -- SCP is located or operates wholly or significantly underground, defined as below the surface of the Earth. Does not apply objects that are simply contained underground for safety or convenience.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/sun sun]** -- SCP is, is related to, or affects a sun, which may or may not be our sun.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/swarm swarm]** -- SCP exhibits swarm behavior.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/tactile tactile]** -- SCP is activated by, triggered by, or affects the sense of touch. Note that this refers specifically to the sense of touch, not simply something that can activate by touching something else.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/telekinetic telekinetic]** -- SCP can manipulate objects or initiate or affect reactions through anomalous means.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/telepathic telepathic]** -- SCP can transfer information via anomalous means.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/teleportation teleportation]** -- SCP can move without occupying intervening space or otherwise displace itself via anomalous means that preclude normal movement.
 * //Avoid using with 'mobile'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/temporal temporal]** -- SCP affects or is otherwise related to the passage of time.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/thermal thermal]** -- SCP is activated by, triggered by, or propagates via changes in temperature. This includes both increases and decreases in temperature.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/thermodynamic thermodynamic]** -- SCP affects, or is otherwise significantly related to the laws of thermodynamics.
 * //Supersedes 'physics'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/timepiece timepiece]** -- SCP is, or a major component of, an instrument or mechanism designed to measure time.
 * //Often used with 'clockwork', and 'mechanical'//
 * //Supersedes 'artifact'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/tool tool]** -- SCP is (or was intended to be) used as a tool.
 * //Supersedes 'artifact'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/toxic toxic]** -- SCP induces chemical toxicity in subjects.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/toy toy]** -- SCP is, or was primarily intended to be, used as a toy.
 * //Supersedes 'artifact'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/transfiguration transfiguration]** -- SCP alters the shape or substance of subjects in an anomalous manner.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/transmission transmission]** -- SCP transmits information, typically via radio waves or other electromagnetic means.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/uncontained uncontained]** -- SCP is neither fully nor partially contained. This should only be applied to SCPs where no instances are contained at all and does not apply if the Foundation successfully contains one or more instances.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/ursine ursine]** -- SCP is or exhibits traits of ursine, or bear-like animals.
 * //Often used with 'animal'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/vehicle vehicle]** -- SCP is or is intended to be used as a vehicle.
 * //Supersedes 'artifact'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/vermian vermian]** -- SCP is or exhibits traits of vermian, or worm-like animals.
 * //Often used with 'animal'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/vibration vibration]** -- SCP generates anomalous vibrations or other repetitive movement.
 * //Often used with 'acoustic'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/virus virus]** -- SCP exhibits traits of viral agents.
 * //Requires either 'biological', or 'computer'//
 * //Supersedes 'contagion'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/visual visual]** -- SCP is triggered by, activated by, or affects the sense of sight.
 * //Often used with 'cognitohazard', and 'sensory'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/weapon weapon]** -- SCP is or is intended to be used as a weapon.
 * //Supersedes 'artifact'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/wooden wooden]** -- SCP is composed primarily or significantly of wood or wood-like material. Should not be used to describe living, unmodified plants that happen to be composed of wood.

[[/tab]]

[[tab Groups of Interest]]
++ Groups of Interest

These tags are used to designate pages that prominently feature a Group of Interest.

* **[https://scp-wiki.wikidot.com/system:page-tags/tag/abnormalities abnormalities]** -- Of of related to the Department of Abnormalities.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/accelerate-the-future accelerate-the-future]** -- Of or related to Accelerate the Future.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/alexylva alexylva]** -- Of or related to the Alexylva University group of interest.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/ambrose-restaurant ambrose-restaurant]** -- Of or related to the Ambrose Restaurant.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/anderson anderson]** -- Of or related to the Anderson Robotics group of interest.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/arcadia arcadia]** -- Of or related to the ##purple|Arcadia## organization.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/are-we-cool-yet are-we-cool-yet]** -- Of or related to the Are We Cool Yet? (AWCY) group of interest.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/asci asci]** -- Of or related to the American Secure Containment Initiative.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/avelar avelar]** -- Of or related to Avelar Professional Products.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/black-queen black-queen]** -- Of or related to the Black Queen group of interest.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/blackwood blackwood]** -- Of or related to The Adventures of Lord Blackwood, Explorer and Gentleman.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/british-occult-service british-occult-service]** -- Of or related to the British Occult Service (MI666) group of interest.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/broken-god broken-god]** -- Of or related to Mekhane, or the Church of the Broken God (CotBG) group of interest.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/brothers-of-death brothers-of-death]** -- Of or related to the Brothers of Death canon or characers.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/chaos-insurgency chaos-insurgency]** -- Of or related to the Chaos Insurgency (CI) group of interest.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/chicago-spirit chicago-spirit]** -- Of or related to the Chicago Spirit group of interest.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/children-of-the-night children-of-the-night]** -- Of or related to the Children of the Night, outlined in [https://scp-wiki.wikidot.com/scp-1000 SCP-1000].
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/children-of-the-torch children-of-the-torch]** -- SCP is of or related to the Children of the Torch group of Interest.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/class-of-76 class-of-76]** -- Of or related to the [https://scp-wiki.wikidot.com/remembrance Class of '76] SCPs and stories.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/daevite daevite]** -- Of or related to the Daevites.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/decommissioning-dept decommissioning-dept]** -- Of or related to the Decommissioning Department.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/deer-college deer-college]** -- Of or related to the Deer College group of interest.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/dr-wondertainment dr-wondertainment]** -- Of or related to the Dr. Wondertainment individual or group of interest.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/ethics-committee ethics-committee]** -- Of or related to the Foundation Ethics Committee.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/factory factory]** -- Of or related to The Factory group of interest.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/fifthist fifthist]** -- Of or related to The Fifthist Church group of interest.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/folklore-dept folklore-dept]** -- Of or related to the Foundation Department of Mythology and Folkloristics.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/gamers-against-weed gamers-against-weed]** -- Of or related to The Gamers Against Weed group of interest.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/global-occult-coalition global-occult-coalition]** -- Of or related to the Global Occult Coalition (GOC) group of interest.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/golden-horde golden-horde]** -- Of or related to the Golden Horde group of interest.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/greazeburger greazeburger]** -- Of or related to the Greazeburger group of interest.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/gru-division-p gru-division-p]** -- Of or related to the GRU Division "P" group of interest.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/herman-fuller herman-fuller]** -- Of or related to the Herman Fuller's Circus of the Disquieting group of interest.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/hmfscp hmfscp]** -- Of or related to His/Her Majesty's Foundation For The Study of Curiosities and Phantasmagoria.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/horizon-initiative horizon-initiative]** -- Of or related to the Horizon Initiative group of interest.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/icsut icsut]** -- Of or related to the International Center for the Study of Unified Thaumatology.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/ijamea ijamea]** -- Of or related to the Imperial Japanese Anomalous Matters Examination Agency.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/madao madao]** -- Of or related to the Italian GoI Medicean Academy of Occult Art (Medicea Accademia Dell'Arte Occulta).
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/mages-academy mages-academy]** -- Of or related to the Mages Academy group of interest.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/manna-charitable-foundation manna-charitable-foundation]** -- Of or related to the Manna Charitable Foundation group of interest.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/marshall-carter-and-dark marshall-carter-and-dark]** -- Of or related to the Marshall, Carter, and Dark Ltd. (MC&D) group of interest.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/miscommunications miscommunications]** -- Of or related to the [https://scp-wiki.wikidot.com/domc-hub Department of Miscommunications].
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/nameless nameless]** -- Of or related to the Nameless, or the Fae, outlined in [https://scp-wiki.wikidot.com/scp-4000 SCP-4000].
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/nobody nobody]** -- Of or related to the 'Nobody' group of interest.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/obearwatch obearwatch]** -- Of or related to the Obearwatch group of interest.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/obskura obskura]** -- Of or related to the Obskura Corps group of interest.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/oneiroi oneiroi]** -- Of or related to the Oneiroi Collective group of interest.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/parawatch parawatch]** -- Of or related to the Parawatch Wiki.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/pattern-screamer pattern-screamer]** -- Of or related to pattern screamers.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/pentagram pentagram]** -- Of or related to Pentagram.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/professor-aw professor-aw]** -- Of or related to the inventions and curiosities of one Professor A. W.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/prometheus prometheus]** -- Of or related to the Prometheus Labs group of interest.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/reclamation reclamation]** -- Of or related to the Office For The Reclamation of Islamic Artifacts (ORIA) group of interest. .
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/sapphire sapphire]** -- Of or related to the SAPPHIRE group of interest. .
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/sarkic sarkic]** -- Of or related to the Sarkic Cults group of interest.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/second-hytoth second-hytoth]** -- Of or related to the Church of the Second Hytoth group of Interest.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/serpents-hand serpents-hand]** -- Of or related to the Serpent's Hand group of interest.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/shark-punching-center shark-punching-center]** -- Of or related to the Shark Punching Center.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/silicon-nornir silicon-nornir]** -- Of or related to the Servants of the Silicon Nornir religion.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/sugarcomb-confectionery sugarcomb-confectionery]** -- Of or related to Sugarcomb Confectionery.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/surrealistics-dept surrealistics-dept]** -- Of or related to the Foundation Department of Surrealistics.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/tactical-theology tactical-theology]** -- Of or related to the Department of Tactical Theology.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/telecom-office telecom-office]** -- Of or related to the Foundation Telecommunications Monitoring Office.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/three-moons-initiative three-moons-initiative]** -- Of or related to the Three Moons Initiative.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/totleighsoft totleighsoft]** -- Of or related to the anomalous software development corporation TotleighSoft.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/unusual-cargo unusual-cargo]** -- Of or related to the Commission on Unusual Cargo.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/unusual-incidents-unit unusual-incidents-unit]** -- Of or related to the Federal Bureau of Investigation Unusual Incidents Unit (UIU) group of interest.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/vikander-kneed vikander-kneed]** -- Of or related to the Vikander-Kneed Technical Media group of interest.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/wandsmen wandsmen]** -- Of of related to the Wandsmen group of interest.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/westhead-media westhead-media]** -- Of or related to the Westhead Media group of interest.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/wilsons-wildlife wilsons-wildlife]** -- Of or related to the Wilson's Wildlife organization.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/xia-dynasty xia-dynasty]** -- Of or related to the Xia Dynasty.

[[/tab]]

[[tab GoI Formats]]
++ GoI Formats

These are tags for GoI formats that describe which GoI the page is formatted for. There should be one tag for each GoI; however, only GoIs for which GoI Format articles exist are listed here. If there is a GoI Format article in the format of a GoI that does not have a tag, it should be tagged //_other//. Additionally, if the corresponding tag for a GoI format does not exist but there is an article that should have it, please contact staff to request it.

[[div class="blockquote"]]
The following applies to all tags in this category:

* Requires 'goi-format'

[[/div]]

* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_alexylva _alexylva]** -- An article following the Alexylva Universiy format.
 * //Requires 'alexylva'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_ambrose-restaurant _ambrose-restaurant]** -- An article following the Ambrose Restaurants format.
 * //Requires 'ambrose-restaurant'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_anderson _anderson]** -- An article following the Anderson Robotics format.
 * //Requires 'anderson'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_arcadia _arcadia]** -- An article following the Arcadia format.
 * //Requires 'arcadia'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_are-we-cool-yet _are-we-cool-yet]** -- An article following the Are We Cool Yet? format.
 * //Requires 'are-we-cool-yet'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_black-queen _black-queen]** -- An article following the Black Queen format.
 * //Requires 'black-queen'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_broken-god _broken-god]** -- An article following the Church of the Broken God format.
 * //Requires 'broken-god'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_chaos-insurgency _chaos-insurgency]** -- An article following the Chaos Insurgency format.
 * //Requires 'chaos-insurgency'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_chicago-spirit _chicago-spirit]** -- An article following the Chicago Spirit format.
 * //Requires 'chicago-spirit'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_deer-college _deer-college]** -- An article following the Deer College format.
 * //Requires 'deer-college'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_eric _eric]** -- An article following the Eric format.
 * //Requires 'eric'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_factory _factory]** -- An article following the Factory format.
 * //Requires 'factory'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_fifthist _fifthist]** -- An article following the Fifthist format.
 * //Requires 'fifthist'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_global-occult-coalition _global-occult-coalition]** -- An article following the Global Occult Coalition format.
 * //Requires 'global-occult-coalition'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_gru-division-p _gru-division-p]** -- An article following the GRU Division P format.
 * //Requires 'gru-division-p'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_herman-fuller _herman-fuller]** -- An article following the Herman Fuller format.
 * //Requires 'herman-fuller'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_horizon-initiative _horizon-initiative]** -- An article following the Horizon Initiative format.
 * //Requires 'horizon-initiative'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_icsut _icsut]** -- An article following the International Center for the Study of Unified Thaumatology.
 * //Requires 'icsut'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_ijamea _ijamea]** -- An article following the IJAMEA format.
 * //Requires 'ijamea'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_la-rue-macabre _la-rue-macabre]** -- An article following the La Rue Macabre format.
 * //Requires 'la-rue-macabre'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_madao _madao]** -- An article following the Medicea Accademia format.
 * //Requires 'madao'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_manna-charitable-foundation _manna-charitable-foundation]** -- An article following the Manna Charitable Foundation format.
 * //Requires 'manna-charitable-foundation'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_marshall-carter-and-dark _marshall-carter-and-dark]** -- An article following the Marshall, Carter and Dark format.
 * //Requires 'marshall-carter-and-dark'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_nobody _nobody]** -- An article following the Nobody format.
 * //Requires 'nobody'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_oneiroi _oneiroi]** -- An article following the Oneiroi format.
 * //Requires 'oneiroi'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_other _other]** -- A GoI Format following a format not associated with a tagged Group of Interest.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_prometheus _prometheus]** -- An article following the Prometheus format.
 * //Requires 'prometheus'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_reclamation _reclamation]** -- An article following the Reclamation format.
 * //Requires 'reclamation'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_sapphire _sapphire]** -- An article following the SAPPHIRE format.
 * //Requires 'sapphire'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_sarkic _sarkic]** -- An article following the Sarkic format.
 * //Requires 'sarkic'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_second-hytoth _second-hytoth]** -- An article following the Second Hytoth format.
 * //Requires 'second-hytoth'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_serpents-hand _serpents-hand]** -- An article following the Serpents' Hand format.
 * //Requires 'serpents-hand'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_shark-punching-center _shark-punching-center]** -- An article following the Shark Punching Center format.
 * //Requires 'shark-punching-center'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_three-moons-initiative _three-moons-initiative]** -- An article following the Three Moons Initiative format.
 * //Requires 'three-moons-initiative'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_unusual-cargo _unusual-cargo]** -- An article following the Unusual Cargo format.
 * //Requires 'unusual-cargo'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_unusual-incidents-unit _unusual-incidents-unit]** -- An article following the Unusual Incidents Unit format.
 * //Requires 'unusual-incidents-unit'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_wandsmen _wandsmen]** -- An article following the Wandsmen format.
 * //Requires 'wandsmen'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_wilsons-wildlife _wilsons-wildlife]** -- An article following the Wilsons' Wildlife format.
 * //Requires 'wilsons-wildlife'//

[[/tab]]

[[tab Canons]]
++ Canons

Tags for canons from the Canon Hub and the articles that take place in their setting.

* **[https://scp-wiki.wikidot.com/system:page-tags/tag/aces-and-eights aces-and-eights]** -- Of or related to the [https://scp-wiki.wikidot.com/aces-and-eights Aces and Eights] canon.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/aiad aiad]** -- Of or related to the [https://scp-wiki.wikidot.com/aiad-homescreen AIAD] canon.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/ad-astra ad-astra]** -- Of or related to the [https://scp-wiki.wikidot.com/ad-astra-per-aspera-hub Ad Astra Per Aspera] canon.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/alchemy-department alchemy-department]** -- Of or related to [https://scp-wiki.wikidot.com/the-alchemy-department-hub The Alchemy Department] canon.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/antarctic-exchange antarctic-exchange]** -- Of or related to the [https://scp-wiki.wikidot.com/antarctic-exchange-hub Antarctic Exchange] canon.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/apotheosis apotheosis]** -- Of or related to the [https://scp-wiki.wikidot.com/antarctic-exchange-hub Apotheosis] canon.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/bellerverse bellerverse]** -- Of or related to the [https://scp-wiki.wikidot.com/bellerverse Bellerverse] canon.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/black-rabbit-company black-rabbit-company]** -- Of or related to the [https://scp-wiki.wikidot.com/stealingsolidarityhub Stealing Solidarity] canon.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/broken-masquerade broken-masquerade]** -- Of or related to the [https://scp-wiki.wikidot.com/broken-masquerade-hub Broken Masquerade] canon.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/competitive-eschatology competitive-eschatology]** -- Of or related to the [https://scp-wiki.wikidot.com/Competitive-Eschatology-Hub Competitive Eschatology] canon.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/cool-war-2 cool-war-2]** -- Of or related to the [https://scp-wiki.wikidot.com/cool-war-2-hub Cool War 2: Ruiz From Your Grave] canon.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/daybreak daybreak]** -- Of or related to the [https://scp-wiki.wikidot.com/daybreak Daybreak] canon.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/deepwell-catalog deepwell-catalog]** -- Of or related to the [https://scp-wiki.wikidot.com/site-17-hub Site-17 Deepwell] canon.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/doctors-of-the-church doctors-of-the-church]** -- Of or related to the [https://scp-wiki.wikidot.com/doctors-of-the-church-hub Doctors of the Church] canon.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/dread&circuses dread&circuses]** -- Of or related to the [https://scp-wiki.wikidot.com/dread-circuses-hub Dread and Circuses] canon.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/end-of-death end-of-death]** -- Of or related to the [https://scp-wiki.wikidot.com/end-of-death-hub End of Death] canon.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/etdp etdp]** -- Of or related to the [https://scp-wiki.wikidot.com/etdp-hub-page Et Tam Deum Petivi] canon.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/from-120s-archives from-120s-archives]** -- Of or related to the [https://scp-wiki.wikidot.com/from-120-s-archives-hub From 120's Archives] canon.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/green-king green-king]** -- Of or related to the [https://scp-wiki.wikidot.com/codename-green-king-hub Codename: Green King hub].
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/heimdall heimdall]** -- Of or related to [https://scp-wiki.wikidot.com/Project-Heimdall Project Heimdall].
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/insect-hell insect-hell]** -- Of or related to the [https://scp-wiki.wikidot.com/arbh-class-hub Insect Hell] canon.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/lolfoundation lolfoundation]** -- Of or related to the [https://scp-wiki.wikidot.com/lolfoundation-hub-page lolFoundation] canon.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/man-who-wasnt-there man-who-wasnt-there]** -- Of or relating to [https://scp-wiki.wikidot.com/the-man-who-wasnt-there-hub The Man Who Wasn't There] canon.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/memoria-adytum memoria-adytum]** -- Of or related to the [https://scp-wiki.wikidot.com/memoria-adytum In Memoria, Adytum] canon.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/no-return no-return]** -- Of or related to the [https://scp-wiki.wikidot.com/no-return-hub No Return] canon.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/old-man-in-the-sea old-man-in-the-sea]** -- Of or related to the [https://scp-wiki.wikidot.com/old-man-in-the-sea-hub Old Man in the Sea] canon.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/on-guard-43 on-guard-43]** -- Of or related to the [https://scp-wiki.wikidot.com/on-guard-43-hub On Guard 43] canon.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/on-mount-golgotha on-mount-golgotha]** -- Of or related to the [https://scp-wiki.wikidot.com/on-mount-golgotha-hub On Mount Golgotha] canon.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/only-game-in-town only-game-in-town]** -- Of or related to the [https://scp-wiki.wikidot.com/only-game-in-town-hub Only Game in Town] canon.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/orcadia orcadia]** -- Of or related to the Seas of Orcadia canon.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/pitch-haven pitch-haven]** -- Of or related to the [https://scp-wiki.wikidot.com/pitch-haven-hub Pitch Haven] canon.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/rats-nest rats-nest]** -- Of or related to the [https://scp-wiki.wikidot.com/rat-s-nest-hub Rat's Nest] canon.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/resurrection resurrection]** -- Of or related to the [https://scp-wiki.wikidot.com/resurrection Resurrection] project.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/s&c-plastics s&c-plastics]** -- Of or related to the [https://scp-wiki.wikidot.com/the-s-c-plastics-hub S & C Plastics] canon.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/ship-in-a-bottle ship-in-a-bottle]** -- Of or related to the [https://scp-wiki.wikidot.com/siabhub Ship In A Bottle] canon.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/sotm sotm]** -- Of or related to the [https://scp-wiki.wikidot.com/sotmhub Straight On Till Morning] canon.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/the-coldest-war the-coldest-war]** -- Of or related to the [https://scp-wiki.wikidot.com/the-coldest-war-hub Coldest War] canon.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/the-gulf the-gulf]** -- Of or related to [https://scp-wiki.wikidot.com/The-Gulf The Gulf] canon.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/the-trashfire the-trashfire]** -- Of or relating to [https://scp-wiki.wikidot.com/the-trashfire The Trashfire] canon.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/third-law third-law]** -- Of or pertaining to the [https://scp-wiki.wikidot.com/third-law-hub Third Law] canon.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/twisted-pines twisted-pines]** -- Of or related to the [https://scp-wiki.wikidot.com/those-twisted-pines-hub Those Twisted Pines] canon.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/unfounded unfounded]** -- Of or related to the [https://scp-wiki.wikidot.com/unfounded-hub Unfounded] canon.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/unhuman unhuman]** -- Of or related to the [https://scp-wiki.wikidot.com/unhuman-hub UnHuman] canon.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/war-on-all-fronts war-on-all-fronts]** -- Of or related to the [https://scp-wiki.wikidot.com/war-on-all-fronts-hub War On All Fronts] canon.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/wonderful-world wonderful-world]** -- Of or related to the [https://scp-wiki.wikidot.com/wonder-world What a Wonderful World] canon.

[[/tab]]

[[tab Tale Series]]
++ Tale Series

Tags for long tale series, that may or may not have a Hub.

* **[https://scp-wiki.wikidot.com/system:page-tags/tag/anabasis anabasis]** -- Of or related to the [https://scp-wiki.wikidot.com/anabasis-hub Anabasis] stories.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/ao-tale ao-tale]** -- Of or related to the [https://scp-wiki.wikidot.com/ao-hub Tales of Anomalous Items] stories.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/classical-revival classical-revival]** -- Of or related to the [https://scp-wiki.wikidot.com/classicalrevivalindex Classical Revival] stories.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/collector-tale collector-tale]** -- Of or related to the Tales of Mr. Collector. (See also: //[https://scp-wiki.wikidot.com/system:page-tags/tag/mister mister]//).
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/goc-casefiles goc-casefiles]** -- Of or related to the [https://scp-wiki.wikidot.com/goc-hub-page#toc111 Global Occult Coalition Casefiles] stories.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/kiryu-labs kiryu-labs]** -- Of or related to the [https://scp-wiki.wikidot.com/kiryu-labs-hub Kiryu Labs] series.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/mister mister]** -- Of or related to the "Little Misters" series of anomalous individuals.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/olympia olympia]** -- Of or related to the [https://scp-wiki.wikidot.com/Olympia-Project Olympia Project].
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/orientation orientation]** -- Of or related to the Orientation series.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/palisade palisade]** -- Of the [https://scp-wiki.wikidot.com/project-palisade Project Palisade] series.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/project-crossover project-crossover]** -- Of or related to [https://scp-wiki.wikidot.com/crossoverprojectindex Project Crossover].
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/project-thaumiel project-thaumiel]** -- Of or related to [https://scp-wiki.wikidot.com/thaumiel Project Thaumiel].
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/team-bird team-bird]** -- Of or related to [https://scp-wiki.wikidot.com/bird Team Bird].

[[/tab]]

[[tab Characters]]
++ Characters

Tags indicating that a specific character has a significant presence within the article. See [https://scp-wiki.wikidot.com/forum/t-1938874/character-tags this thread] for further details.

* **[https://scp-wiki.wikidot.com/system:page-tags/tag/8-ball 8-ball]** -- 8-ball, aka 8B-A1.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/aaron-siegel aaron-siegel]** -- Aaron Siegel.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/able able]** -- Able, aka SCP-076.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/agent-green agent-green]** -- Agent Green.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/agent-kazmarek agent-kazmarek]** -- Agent Travis Kazmarek.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/agent-laferrier agent-laferrier]** -- Agent V.A. LaFerrier.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/agent-lament agent-lament]** -- Agent Troy Lament.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/agent-lurk agent-lurk]** -- Agent Dietrich M. Lurk.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/agent-merlo agent-merlo]** -- Agent Sasha Merlo.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/agent-navarro agent-navarro]** -- Agent Daniel Navarro.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/agent-popescu agent-popescu]** -- Agent Lucretia Popescu.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/agent-strelnikov agent-strelnikov]** -- Agent Dmitri Strelnikov.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/agent-trauss agent-trauss]** -- Agent Trauss, aka C-51174.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/agent-yoric agent-yoric]** -- Agent Yoric Elroy, aka Jack "Poor Yoric" Dawkins.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/aldon aldon]** -- Aldon.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/alexandra alexandra]** -- Alexandra, AI unit.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/alexei-belitrov alexei-belitrov]** -- Alexei Belitrov, aka SCP-2273.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/alleged-god alleged-god]** -- SCP-343, aka "God".
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/bailey-brothers bailey-brothers]** -- Tristan, Thomas and Trevor Bailey.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/big-cheese-horace big-cheese-horace]** -- Big Cheese Horace of the Fifthists.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/bobble-the-clown bobble-the-clown]** -- Bobble The Clown, aka SCP-993.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/bones bones]** -- Bones, aka SCP-2721-LORD or Eli.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/brainy-brian brainy-brian]** -- Brainy Brian of Wondertainment/MC&D, also known as 'Doctor Neurosis'.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/cain cain]** -- Cain, aka SCP-073.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/chaz-ambrose chaz-ambrose]** -- Chaz Ambrose, founder of Ambrose Restaurants.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/cousin-johnny cousin-johnny]** -- Cousin Johnny, aka SCP-2852.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/d-7294 d-7294]** -- D-7294.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/d-11424 d-11424]** -- D-11424.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/dado dado]** -- dado is taking care of u in dis one. u no worry.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/dc-al-fine dc-al-fine]** -- D.C. al Fine, Undersecretary-General of the Global Occult Coalition.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/director-aktus director-aktus]** -- Director Aktus.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/director-bold director-bold]** -- Director Cal Bold of the Decommissioning Department.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/director-diaghilev director-diaghilev]** -- Director Ruslav Diaghilev of the Alchemy Department.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/director-gillespie director-gillespie]** -- Director Gillespie.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/director-mcinnis director-mcinnis]** -- Dr. Allan J. McInnis, Director of Site-43.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/director-mctiriss director-mctiriss]** -- Director Kate McTiriss.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/director-moose director-moose]** -- Director Moose.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/director-lague director-lague]** -- Director Paul Lague, of the Integration Program and Site-322.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/django-bridge django-bridge]** -- Django Bridge.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/doctor-asheworth doctor-asheworth]** -- Dr. Daniel Asheworth.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/doctor-blank doctor-blank]** -- Dr. Harold R. Blank.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/doctor-bright doctor-bright]** -- Dr. Bright.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/doctor-cimmerian doctor-cimmerian]** -- Dr. Cimmerian.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/doctor-clef doctor-clef]** -- Dr. Alto Clef.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/doctor-dan doctor-dan]** -- Dr. Dan ███████, of SCP-096.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/doctor-edison doctor-edison]** -- Dr. Michael Edison.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/doctor-elliott doctor-elliott]** -- Dr. Chelsea Elliott.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/doctor-everwood doctor-everwood]** -- Dr. Everwood, GOI specialist.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/doctor-fynegan doctor-fynegan]** -- Dr. Fynegan.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/doctor-gears doctor-gears]** -- Dr. Gears.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/doctor-gerald doctor-gerald]** -- Dr. Gerald.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/doctor-glass doctor-glass]** -- Dr. Simon Glass.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/doctor-heiden doctor-heiden]** -- Dr. Frederick Heiden.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/doctor-hoygull doctor-hoygull]** -- Dr. Hoygull, Avian Division.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/doctor-iceberg doctor-iceberg]** -- Dr. Iceberg.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/doctor-king doctor-king]** -- Dr. King.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/doctor-kondraki doctor-kondraki]** -- Dr. Kondraki.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/doctor-light doctor-light]** -- Dr. Sophia N. Light.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/doctor-lillihammer doctor-lillihammer]** -- Dr. Lillian S. Lillihammer.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/doctor-mann doctor-mann]** -- Dr. Everett Mann.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/doctor-mcdoctorate doctor-mcdoctorate]** -- Dr. Placeholder McDoctorate.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/doctor-reynders doctor-reynders]** -- Dr. Ilse Reynders.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/doctor-rights doctor-rights]** -- Dr. Rights.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/doctor-rivera doctor-rivera]** -- Dr. Jessie Rivera.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/doctor-roget doctor-roget]** -- Dr. Ralph Roget.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/doctor-thereven doctor-thereven]** -- Doctor Cole Thereven.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/doctor-sinclair doctor-sinclair]** -- Dr. Katherine Sinclair.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/doctor-sorts doctor-sorts]** -- Dr. Johannes Sorts.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/doctor-spanko doctor-spanko]** -- Dr. Spanko.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/doctor-vang doctor-vang]** -- Dr. S. Vang.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/doctor-wettle doctor-wettle]** -- Dr. William Wallace Wettle.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/donkman donkman]** -- Ulysses B. Donkman.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/draven-kondraki draven-kondraki]** -- Dr./Director Draven Kondraki.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/eric eric]** -- Eric, a mysterious character.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/esther-kogan esther-kogan]** -- Esther Kogan, aka lesbian_gengar of Gamers Against Weed.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/faeowynn-wilson faeowynn-wilson]** -- Faeowynn "Fae" Wilson.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/finnegan finnegan]** -- Finnegan.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/fred fred]** -- Fred, aka SCP-423.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/general-bowe general-bowe]** -- General Bowe.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/glacon glacon]** -- Glacon.aic.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/grabnok grabnok]** -- Grabnok the Destroyer, aka SCP-507.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/grand-karcist-ion grand-karcist-ion]** -- Grand Karcist Ion, a Sarkic figure.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/halyna-ieva halyna-ieva]** -- Karcist Halyna Ieva, aka The Mother Who Demands One's Toes.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/hanged-king hanged-king]** -- Of or relating to the Hanged King.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/hard-to-kill-reptile hard-to-kill-reptile]** -- The "Hard-To-Destroy Reptile", aka SCP-682.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/heather-mason heather-mason]** -- Heather Mason, aka "Ms. Mad About Video Games" or SCP-3090.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/holly-light holly-light]** -- Holly Light.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/icky icky]** -- Veronica the Magic Clown.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/iris-dark iris-dark]** -- Iris Dark.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/iris-thompson iris-thompson]** -- Iris Thompson, aka SCP-105.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/isabel-v isabel-v]** -- Isabel Helga Anastasia Parvati Wondertainment V.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/jockjamsvol6 jockjamsvol6]** -- JJ, AKA jockjamsvol6 of Gamers Against Weed.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/jude-kriyot jude-kriyot]** -- Jude Kriyot, AKA bluntfiend of Gamers Against Weed.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/judith-low judith-low]** -- Dr. Judith Low, Department of History.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/judy-papill judy-papill]** -- Judy Papill, AKA Judy the Tongue.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/kain-pathos-crow kain-pathos-crow]** -- Professor Kain Pathos Crow.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/kenneth-spencer kenneth-spencer]** -- Kenneth Spencer.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/kindness kindness]** -- A kind man.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/legate-trunnion legate-trunnion]** -- Legate Trunnion, prophet of the Cogwork Orthodoxy.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/leslie leslie]** -- Leslie, instance of SCP-3774.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/lewitt-zairi-family lewitt-zairi-family]** -- The Lewitt Zairi Family.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/lombardi lombardi]** -- [https://scp-wiki.wikidot.com/the-lombardi-tales Agent Lombardi].
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/manny manny]** -- Manny, aka The Man With the Upside Down Face of Herman Fuller.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/maria-jones maria-jones]** -- Maria Jones of RAISA.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/marion-wheeler marion-wheeler]** -- Marion Wheeler.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/mark-kiryu mark-kiryu]** -- Mark Kiryu of Kiryu Labs.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/moon-champion moon-champion]** -- Moon Champion, aka Champion of the Moon or SCP-1233.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/mr-fish mr-fish]** -- Mr. Fish, Little Mister from Dr. Wondertainment and SCP-527.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/pangloss pangloss]** -- Of or related to the Pangloss individual of interest.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/plague-doctor plague-doctor]** -- The Plague Doctor, aka SCP-049.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/possessive-mask possessive-mask]** -- The Possessive Mask, aka SCP-035.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/professor-bjornsen professor-bjornsen]** -- Professor Anders Bjornsen.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/rainer-miller rainer-miller]** -- Rainer Miller, aka SCP-4051.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/researcher-conwell researcher-conwell]** -- Researcher Jacob Conwell.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/researcher-james researcher-james]** -- Junior Researcher James, best foundation researcher ever! (Age 5).
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/researcher-labelle researcher-labelle]** -- Researcher Rose Labelle.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/researcher-lloyd researcher-lloyd]** -- Researcher Lloyd, Destroyer of Worlds.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/researcher-rosen researcher-rosen]** -- Researcher David Rosen.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/researcher-smalls researcher-smalls]** -- Researcher Adamo Smalls.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/researcher-talloran researcher-talloran]** -- Researcher Talloran.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/richard-chappell richard-chappell]** -- Richard Davis Chappell, founder of the Chicago Spirit.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/riven-mercer riven-mercer]** -- Riven Mercer of Kiryu Labs.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/robert-bumaro robert-bumaro]** -- Robert Bumaro, a prophet of Mekhane.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/robin-thorne robin-thorne]** -- Robin Thorne.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/ruiz-duchamp ruiz-duchamp]** -- Ruiz Duchamp, an anartist.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/saint-hedwig saint-hedwig]** -- Saint Hedwig, a prophet of Maxwellism.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/saturn-deer saturn-deer]** -- Saturn Deer.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/scarlet-king scarlet-king]** -- The Scarlet King.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/sheldon-katz sheldon-katz]** -- Sheldon Katz.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/shy-guy shy-guy]** -- The Shy Guy, aka SCP-096.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/sigurros sigurros]** -- Sigurrós Stefánsdóttir, aka SCP-239.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/simon-pietrykau simon-pietrykau]** -- Simon Pietrykau.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/tau-5-samsara tau-5-samsara]** -- Mobile Task Force Tau-5 'Samsara'.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/thad-xyank thad-xyank]** -- Dr. Thaddeus "Thad" Xyank.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/the-administrator the-administrator]** -- The Administrator (as a separate entity from the O5 Council).
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/the-engineer the-engineer]** -- The Engineer, of the Chaos Insurgency.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/the-old-man the-old-man]** -- The Old Man, aka SCP-106.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/the-sculpture the-sculpture]** -- The sculpture, aka SCP-173.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/the-specter the-specter]** -- The Specter, aka SCP-4944.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/thilo-zwist thilo-zwist]** -- Thilo Zwist.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/tim-wilson tim-wilson]** -- Tim Wilson, of Wilson's Wildlife Solutions.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/veronica-fitzroy veronica-fitzroy]** -- Veronica Katherine Fitzroy, anartist/d-class.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/vincent-anderson vincent-anderson]** -- Vincent Anderson, of Anderson Robotics.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/zyn-kiryu zyn-kiryu]** -- Researcher Zyn Kiryu.

[[/tab]]

[[tab Locations]]
++ Locations

Tags indicating that a tale or SCP article takes place in a specific location that isn't a Foundation Site or installation.

* **[https://scp-wiki.wikidot.com/system:page-tags/tag/alagadda alagadda]** -- The kingdom of Alagadda.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/backdoor-soho backdoor-soho]** -- The city of Backdoor Soho.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/esterberg esterberg]** -- The Free Port known as Esterberg.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/eurtec eurtec]** -- The metropolis of Eurtec.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/hy-brasil hy-brasil]** -- The island of Hy-Brasil.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/la-rue-macabre la-rue-macabre]** -- The free port of La Rue Macabre.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/three-portlands three-portlands]** -- The city of Three Portlands.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/wanderers-library wanderers-library]** -- The Wanderer's Library.

[[/tab]]

[[tab Content Markers]]
++ Content Markers

Tags for noting specific content.

* **[https://scp-wiki.wikidot.com/system:page-tags/tag/adult adult]** -- Denotes mature content, view at your own discretion.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/audio audio]** -- //audio// pages are pages with one or more audio files attached.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/interactive interactive]** -- The article contains elements that require user input or interaction, e.g. making a decision (making the user click a single link or open a collapsible does not count).
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/video video]** -- //video// pages are pages with one or more video files attached.

[[/tab]]

[[tab Staff Process]]
++ Staff Process

These tags are added only used by SCP Wiki staff, and are intended to designate articles under staff process.

* **[https://scp-wiki.wikidot.com/system:page-tags/tag/in-rewrite in-rewrite]** -- This is a temporary tag that may be placed on an article //by members of the Rewrite Team// only. It indicates the article is currently being rewritten and should be removed when said rewrite is posted. It should only be placed on articles where for reasons of site history, the original article will not be deleted before the rewrite is posted.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/rewritable rewritable]** -- This is a temporary tag that may be be placed on an article //by members of the Rewrite Team// only. It indicates that the article is eligible to be rewritten due to circumstances falling outside the usual case of low rating and old age.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/rewrite rewrite]** -- This tag indicates that the article in question is a rewrite of another article.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/in-deletion in-deletion]** -- This is a temporary tag that indicates the article is currently being voted on for deletion. It should only be placed on articles where a deletion vote has been started. Other tags should be removed when this tag is added to a page. Remove if deletion is permanently cancelled for whatever reason.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/featured featured]** -- Designates [https://scp-wiki.wikidot.com/featured-scp-archive Featured Articles] and [https://scp-wiki.wikidot.com/featured-tale-archive Featured Tales].
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/prize-feature prize-feature]** -- Designates articles featured by the winner of a site contest.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/reviewers-spotlight reviewers-spotlight]** -- Designates articles featured by a [https://scp-wiki.wikidot.com/reviewers-spotlight-archive forum reviewer].
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/event-featured event-featured]** -- Designates articles featured on special event days such as International Talk Like a Pirate Day.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/metadata metadata]** -- Designates pages with meta information about articles.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_cc _cc]** -- This tag indicates that all images on the page in question have been demonstrated to be fully compliant with current licensing policy. __This tag should **only** be added by a member of the Licensing team__. This tag conflicts with _image.
 * //Conflicts with '_image'//
 * //Supersedes '_image'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_image _image]** -- This is a temporary tag that the tagging team applies to new articles that include one or more images, irrespective of whatever licensing information is provided by the author. This tag acts as an indicator to the Licensing team that there are images whose license status need to be confirmed and/or verified. Licensing will remove the _image tag and replace it with the _cc tag (or, if images are removed, no tag at all) when appropriate.
 * //Conflicts with '_cc'//
 * //Superseded by '_cc'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_licensebox _licensebox]** -- A tag for designating that an article has a standard license info block that is tracked on the [https://scp-wiki.wikidot.com/licensing-master-list Licensing Master List].
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_listpages _listpages]** -- A tag to denote that this page is an LPT article. LPT (ListPages Presented Text) means that the article presents its content through offsets served via ListPages.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_theme-temp _theme-temp]** -- Temporary tag used for marking old theme locations while they were moved from the {{component:}} category to the {{theme:}} category.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/crosslink crosslink]** -- This is a temporary tag that indicates the Wikiwalk Subteam of MAST is currently proposing revisions on the page, which should be seen in the comments.

[[/tab]]

[[tab Events]]
++ Events

Tags for all events on the wiki, including contests.

* **[https://scp-wiki.wikidot.com/system:page-tags/tag/173fest 173fest]** -- An entry to the [https://scp-wiki.wikidot.com/173-festival 173 Festival].
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/art-exchange art-exchange]** -- Of or related to the [https://scp-wiki.wikidot.com/art-exchange-hub Annual Holiday Art Exchange].
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/af2014 af2014]** -- Of or related to the [https://scp-wiki.wikidot.com/april-fools-2014 Super Cute Pets!] 2014 April Fool's prank.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/game-day game-day]** -- Of or related to the [https://scp-wiki.wikidot.com/gamedayindex Game Day] project.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/nightmarefest nightmarefest]** -- An entry to the unofficial [https://scp-wiki.wikidot.com/nightmarefest NIGHTMAREFEST].
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_townhouse _townhouse]** -- An entry to the 'Townhouse' category of the unofficial NIGHTMAREFEST.
 * //Requires 'nightmarefest'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_the-bureaucrat _the-bureaucrat]** -- An entry to the 'The Bureaucrat' category of the unofficial NIGHTMAREFEST.
 * //Requires 'nightmarefest'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_graveyard-shift _graveyard-shift]** -- An entry to the 'Graveyard Shift' category of the unofficial NIGHTMAREFEST.
 * //Requires 'nightmarefest'//

+++ Contests

Tags for contests and the articles submitted to them.

* **[https://scp-wiki.wikidot.com/system:page-tags/tag/1000 1000]** -- An entry to the [https://scp-wiki.wikidot.com/forum/t-376556 SCP-1000 Contest].
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/2000 2000]** -- An entry to the [https://scp-wiki.wikidot.com/scp2000contesthub SCP-2000 Contest].
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/3000 3000]** -- An entry to the [https://scp-wiki.wikidot.com/scp3000contesthub SCP-3000 Contest].
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/4000 4000]** -- An entry to the [https://scp-wiki.wikidot.com/scp4000contesthub SCP-4000 Contest].
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/5000 5000]** -- An entry to the [https://scp-wiki.wikidot.com/scp5000contesthub SCP-5000 Contest].
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/6000 6000]** -- An entry to the [https://scp-wiki.wikidot.com/scp6000contesthub SCP-6000 Contest].
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/af2016 af2016]** -- An entry to the [https://scp-wiki.wikidot.com/an-incredibly-important-announcement Crack Fiction Contest] 2016 April Fool's prank.
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/art2017 art2017]** -- An entry to the [https://scp-wiki.wikidot.com/social-media-art-contest 2017 Art Contest].
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/canon2020 canon2020]** -- An entry to the [https://scp-wiki.wikidot.com/canon-renaissance-contest 2020 Canon Renaissance Contest].
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/cliche2019 cliche2019]** -- An entry to [https://scp-wiki.wikidot.com/cliche-con-2019 Cliche-Con 2019].
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/collab-con2019 collab-con2019]** -- An entry to [https://scp-wiki.wikidot.com/collaboration-contest Collab-Con 2019].
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/cupid2021 cupid2021]** -- An entry to [https://scp-wiki.wikidot.com/cupid-contest-2021 Cupid Contest 2021].
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/d-con2016 d-con2016]** -- An entry to the [https://scp-wiki.wikidot.com/d-class-contest 2016 D-Class Contest].
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/dc2014 dc2014]** -- An entry to the [https://scp-wiki.wikidot.com/Dystopia-Contest 2014 Dystopia Contest].
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/departmentcon2022 departmentcon2022]** -- An entry to the [https://scp-wiki.wikidot.com/department-contest 2022 Department Contest].
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/doomsday2018 doomsday2018]** -- An entry to the [https://scp-wiki.wikidot.com/doomsday-contest 2018 Doomsday Contest].
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/exquisite-corpse2020 exquisite-corpse2020]** -- An entry to the [https://scp-wiki.wikidot.com/exquisite-corpse-contest 2020 Exquisite Corpse Contest].
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/five-questions five-questions]** -- An entry to the [https://scp-wiki.wikidot.com/five-questions Five Questions Contest].
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/gbc09 gbc09]** -- An entry to [https://scp-wiki.wikidot.com/gears-birthday-contest-2009 2009 Gears' Birthday Contest].
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/goi2014 goi2014]** -- An entry to the [https://scp-wiki.wikidot.com/goi-contest-2014 2014 Groups of Interest Contest].
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/goi2019 goi2019]** -- An entry to the [http://scp-int.wikidot.com/international-goi-contest-2019 International Groups of Interest Contest 2019].
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/halloween2018 halloween2018]** -- An entry to the [https://scp-wiki.wikidot.com/halloween-contest-2018 2018 Halloween Contest].
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/hc2012 hc2012]** -- An entry to the [https://scp-wiki.wikidot.com/halloween-contest 2012 Halloween Contest].
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/hiscon2017 hiscon2017]** -- An entry to the [https://scp-wiki.wikidot.com/history-contest 2017 History Contest].
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/jam-con2018 jam-con2018]** -- An entry to the [https://scp-wiki.wikidot.com/72-hour-jam-contest 2018 72 Hour Jam Contest].
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_dark-and-stormy _dark-and-stormy]** -- An entry to the 'Dark and Stormy' category of the 2018 72 Hour Jam Contest.
 * //Requires 'jam-con2018'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_murder-mystery _murder-mystery]** -- An entry to the 'Murder Mystery' category of the 2018 72 Hour Jam Contest.
 * //Requires 'jam-con2018'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_tropical _tropical]** -- An entry to the 'Tropical' category of the 2018 72 Hour Jam Contest.
 * //Requires 'jam-con2018'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/jam-con2019 jam-con2019]** -- An entry to the [https://scp-wiki.wikidot.com/144-hour-jam-contest 2019 144-Hour Jam Contest].
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_shaggy-dog _shaggy-dog]** -- An entry to the 'Shaggy Dog' category of the 2019 144 Hour Jam Contest.
 * //Requires 'jam-con2019'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_pulp-fiction _pulp-fiction]** -- An entry to the 'Pulp Fiction' category of the 2019 144 Hour Jam Contest.
 * //Requires 'jam-con2019'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_all-a-dream _all-a-dream]** -- An entry to the 'All a Dream' category of the 2019 144 Hour Jam Contest.
 * //Requires 'jam-con2019'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/jam-con2020 jam-con2020]** -- An entry to the [https://scp-wiki.wikidot.com/144-hour-jam-contest-two 2020 144-Hour Jam Contest].
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_explosions _explosions]** -- An entry to the 'Explosions' category of the 2020 144 Hour Jam Contest.
 * //Requires 'jam-con2020'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_delicious _delicious]** -- An entry to the 'Delicious' category of the 2020 144 Hour Jam Contest.
 * //Requires 'jam-con2020'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_meets-the-eye _meets-the-eye]** -- An entry to the 'Meets the Eye' category of the 2020 144 Hour Jam Contest.
 * //Requires 'jam-con2020'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/jam-con2021 jam-con2021]** -- An entry to [http://scp-wiki.wikidot.com/jam-con-2021 JamCon 2021].
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_marine _marine]** -- An entry to the 'Marine' category of JamCon 2021.
 * //Requires 'jam-con2021'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_corruption _corruption]** -- An entry to the 'Corruption' category of JamCon 2021.
 * //Requires 'jam-con2021'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_famouslastwords _famouslastwords]** -- An entry to the '"What could possibly go wrong?"' category of JamCon 2021.
 * //Requires 'jam-con2021'//
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/mtf2016 mtf2016]** -- An entry to the [https://scp-wiki.wikidot.com/mobile-task-force-contest 2016 Mobile Task Force Contest].
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/nyc2013 nyc2013]** -- An entry to the [https://scp-wiki.wikidot.com/new-years-contest 2013 New Year's Canon Contest].
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/rei2015 rei2015]** -- An entry to the [https://scp-wiki.wikidot.com/reimagining-contest 2015 Reimagining Contest].
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/sc2015 sc2015]** -- An entry to the [https://scp-wiki.wikidot.com/short-works-contest 2015 Short Works Contest].
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/tc2013 tc2013]** -- An entry to the [https://scp-wiki.wikidot.com/time-contest 2013 Time Contest].
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/uac2014 uac2014]** -- An entry to the [https://scp-wiki.wikidot.com/under-appreciated-contest 2014 Under-Appreciated SCPs Contest].
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/memecon2021-unofficial memecon2021-unofficial]** -- An entry to the unofficial [https://scp-wiki.wikidot.com/memecon-unofficial 2021 MEMECON].

[[/tab]]

[[tab Translation]]
++ Translation

These tags indicate that the article in question has been translated to SCP-EN from one of the official SCP translation sites.

* **[https://scp-wiki.wikidot.com/system:page-tags/tag/international international]** -- Applicable if the tale or SCP article was translated from one of the recognized translation sites. Don't add this tag if the article //was// translated to another language.

+++ Language Codes

[[div class="blockquote"]]
The following applies to all tags in this section:

* Requires 'international'

[[/div]]

* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_int _int]** -- Translated from the [http://scp-int.wikidot.com/ International Site].
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_ru _ru]** -- Translated from the [http://scpfoundation.net/ Russian Site].
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_ko _ko]** -- Translated from the [http://scpko.wikidot.com/ Korean Site].
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_cn _cn]** -- Translated from the [http://scp-wiki-cn.wikidot.com/ Chinese Site].
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_fr _fr]** -- Translated from the [http://fondationscp.wikidot.com/ French Site].
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_pl _pl]** -- Translated from the [http://scp-wiki.net.pl/ Polish Site].
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_es _es]** -- Translated from the [http://lafundacionscp.wikidot.com/ Spanish Site].
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_th _th]** -- Translated from the [http://scp-th.wikidot.com/main Thai Site].
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_jp _jp]** -- Translated from the [http://scp-jp.wikidot.com/ Japanese Site].
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_de _de]** -- Translated from the [http://scp-wiki-de.wikidot.com/ German Site].
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_it _it]** -- Translated from the [http://fondazionescp.wikidot.com/ Italian Site].
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_ua _ua]** -- Translated from the [http://scp-ukrainian.wikidot.com/ Ukrainian Site].
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_pt _pt]** -- Translated from the [http://scp-pt-br.wikidot.com/ Portuguese Site].
* **[https://scp-wiki.wikidot.com/system:page-tags/tag/_zh _zh]** -- Translated from the [http://scp-zh-tr.wikidot.com/ Traditional Chinese Site].

[[/tab]]

[[/tabview]]

[[collapsible show="+ Show Tag Search TOML" hide="- Hide Tag Search TOML"]]
This is a [https://toml.io/en/ TOML] configuration autogenerated based on the Tag Manifest. It's utilized by [https://crom.wikidot.com/tag-search Crom Tag Search] to provide plaintext descriptions of tags for end users.
[[code]]
[[tags]]
name = "scp"
description = "Used for pages which are SCP articles, including 001 proposals, jokes, and explained articles."

[[tags]]
name = "goi-format"
description = "Used for pages which have been written up from the perspective of a specific Group of Interest, and conforms to the format(s) laid out in that GoI's hub page."

[[tags]]
name = "tale"
description = "Any fiction that is set in the SCP universe but is not an SCP, GoI Format, site page or supplement."

[[tags]]
name = "supplement"
description = "Used for pages which require context from their parent page to understand."

[[tags]]
name = "site"
description = "Used for pages which document specific Foundation facilities, and provide information such as the objects stored at the site, site history, assigned personnel, etc."

[[tags]]
name = "guide"
description = "Used for writing guides, helpful hints, or other pages intended to assist site."

[[tags]]
name = "essay"
description = "Used for useful information on specific topics. They are subjective and reflect the author's personal opinion."

[[tags]]
name = "news"
description = "Pages containing news, updates, or happenings on the SCP Foundation."

[[tags]]
name = "resource"
description = "Pages listing aspects of the SCP canon."

[[tags]]
name = "author"
description = "Used for author profile pages."

[[tags]]
name = "artist"
description = "Used for artist profile pages. Users may have multiple with staff permission."

[[tags]]
name = "artwork"
description = "Used to host Foundation-related artwork created by community members, whether as individual pieces or collections."

[[tags]]
name = "component"
description = "Used for pages intended to be imported onto other pages in order to add new design, style, or functionality."

[[tags]]
name = "component-backend"
description = "Used for internal template pages, intended to only be imported onto other component pages."

[[tags]]
name = "theme"
description = "Theme pages are templates that modify the general look and feel of a page."

[[tags]]
name = "fragment"
description = "Used for pages designed to be imported onto a single page. They should generally not be viewed directly."

[[tags]]
name = "more-by"
description = "Used for pages that lists work by a single author, designed to be imported onto that author's published works on the Wiki."

[[tags]]
name = "forum"
description = "Used for pages which are required for internal functioning of Wikidot's forum system."

[[tags]]
name = "splash"
description = "Used for 'cover pages' for certain articles."

[[tags]]
name = "admin"
description = "Used for pages which have official significance."

[[tags]]
name = "hub"
description = "Used for pages with a large number of links to related pages."

[[tags]]
name = "workbench"
description = "Used for pages created by mods and admins to utilize Wikidot modules."

[[tags]]
name = "sandbox"
description = "Used for pages on the site which are sandboxes."

[[tags]]
name = "joke"
description = "Used for pages which are considered 'jokes' or explicitly 'out-of-universe'. These can be parodies of any page type."

[[tags]]
name = "poetry"
description = "Applicable if the page consists significantly of a form of poetry, with elements such as meter and rhyme."

[[tags]]
name = "archived"
description = "Used for pages which have been archived due to having been superseded, obsoleted, or inactivity."

[[tags]]
name = "explained"
description = "Used for explained SCP articles."

[[tags]]
name = "decommissioned"
description = "Indicates the SCP has been destroyed in-universe upon article deletion out-of-universe."

[[tags]]
name = "001-proposal"
description = "Used for articles proposing a possible SCP-001 object."

[[tags]]
name = "creepypasta"
description = "Used for fiction unrelated to the SCP Foundation, and usually take the form of urban myths or campfire stories."

[[tags]]
name = "collaboration"
description = "Used for pages which are or were previously open to additions from any member, with the caveat that staff and the original author reserve the right to modify or delete entries found to be subpar."

[[tags]]
name = "co-authored"
description = "Used for pages which are the result of two or more authors working together, but are not open to additions from other members."

[[tags]]
name = "contest"
description = "Used for pages which are created for community contests."

[[tags]]
name = "required"
description = "Used for pages which are part of the required reading for joining the SCP Wiki."

[[tags]]
name = "redirect"
description = "Used for pages which redirect the user to a different page."

[[tags]]
name = "_tale-hub"
description = "Used for hubs which represent a series that consists mostly or entirely of tale articles."

[[tags]]
name = "experiment"
description = "Used for supplements containing primarily experiment logs."

[[tags]]
name = "exploration"
description = "Used for supplements containing primarily exploratino logs."

[[tags]]
name = "incident"
description = "Used for supplements containing primarily incident logs or transcripts."

[[tags]]
name = "interview"
description = "Used for supplements containing primarily interview transcripts."

[[tags]]
name = "safe"
description = "SCP is Safe."

[[tags]]
name = "euclid"
description = "SCP is Euclid."

[[tags]]
name = "keter"
description = "SCP is Keter."

[[tags]]
name = "thaumiel"
description = "SCP is Thaumiel."

[[tags]]
name = "apollyon"
description = "SCP is Apollyon."

[[tags]]
name = "archon"
description = "SCP is Archon."

[[tags]]
name = "neutralized"
description = "SCP is Neutralized."

[[tags]]
name = "pending"
description = "SCP is pending classification."

[[tags]]
name = "esoteric-class"
description = "SCP has a non-standard object class or combination."

[[tags]]
name = "acoustic"
description = "SCP is composed of, affects, generates, or is propagated by sound waves."

[[tags]]
name = "adaptive"
description = "SCP adapts to stimuli in an anomalous manner."

[[tags]]
name = "addictive"
description = "SCP causes desire or addictive behavior in affected subjects."

[[tags]]
name = "airborne"
description = "SCP lives in, moves through, or spreads through the air."

[[tags]]
name = "alive"
description = "SCP is alive, meaning it exhibits the biological traits of metabolism, reaction, and reproduction."

[[tags]]
name = "amorphous"
description = "SCP lacks a set form or shape, constantly changes shape, or has a poorly-defined shape e.g. a blob."

[[tags]]
name = "animal"
description = "SCP is or exhibits traits of animal life."

[[tags]]
name = "antimemetic"
description = "SCP is or involves the use of (an) antimeme(s) to suppress knowledge and/or understanding of an idea or concept, including itself."

[[tags]]
name = "apian"
description = "SCP is or exhibits traits of apian or bee-like animals."

[[tags]]
name = "appliance"
description = "SCP is or resembles a household or domestic appliance."

[[tags]]
name = "aquatic"
description = "SCP lives in, moves through or spreads through water."

[[tags]]
name = "arachnid"
description = "SCP is or exhibits traits of arachnid or spider-like animals."

[[tags]]
name = "arboreal"
description = "SCP is or exhibits traits of arboreal or tree-like plants."

[[tags]]
name = "arthropod"
description = "SCP is or exhibits traits of arthropods or animals with exoskeletons, segmented bodies, and jointed appendages."

[[tags]]
name = "artistic"
description = "SCP is a work of art, exhibits artistic properties, or has artistic significance."

[[tags]]
name = "artifact"
description = "SCP is or was originally created by humans."

[[tags]]
name = "auditory"
description = "SCP is triggered by, activated by, or affects the sense of hearing."

[[tags]]
name = "automaton"
description = "SCP is a device or construct designed to operate on its own. Should be applied to anything that can be described as a 'robot'."

[[tags]]
name = "autonomous"
description = "SCP activates/operates on its own in an anomalous fashion. Only applicable to objects that normally do not activate on their own."

[[tags]]
name = "avian"
description = "SCP is or exhibits traits of avian or bird-like animals."

[[tags]]
name = "bacteria"
description = "SCP is, resembles, or exhibits traits of a bacterial life-form."

[[tags]]
name = "bibliothetic"
description = "SCP is, or is otherwise related to or affects libraries, defined as a room or building containing books for people to read or borrow."

[[tags]]
name = "biohazard"
description = "SCP poses a hazard to humans or the environment as a result of biological function, or is a biological hazard."

[[tags]]
name = "biological"
description = "SCP exhibits biological traits."

[[tags]]
name = "bovine"
description = "SCP is or exhibits traits of bovine or cattle-like animals."

[[tags]]
name = "building"
description = "SCP is, is a part of, or otherwise is related to or affects a building, defined as a structure intended for human occupation."

[[tags]]
name = "cadaver"
description = "SCP is, affects, or is related to corpses, carcasses, or any dead organic matter."

[[tags]]
name = "canine"
description = "SCP is or exhibits traits of canine or dog-like animals."

[[tags]]
name = "carnivorous"
description = "SCP is or exhibits traits of carnivorous animals."

[[tags]]
name = "cervine"
description = "SCP is or exhibits traits of cervine or deer-like animals. Also includes elk and moose."

[[tags]]
name = "cephalopodic"
description = "SCP is or exhibits traits of cephalopods or animals including the cuttlefish, octopus, and squid."

[[tags]]
name = "cetacean"
description = "SCP is or exhibits traits of cetacean or whale-like animal."

[[tags]]
name = "chemical"
description = "SCP is an anomalous chemical compound or produces chemical compounds in an anomalous way."

[[tags]]
name = "city"
description = "SCP is a city, town, or other settlement intended for human occupation. Should only be used if a significant portion of the city is considered anomalous."

[[tags]]
name = "clay"
description = "SCP is primarily or significantly composed of clay."

[[tags]]
name = "clockwork"
description = "SCP operates primarily via clockworks, defined as mechanical devices constructed primarily using toothed wheels and/or powered by a mainspring."

[[tags]]
name = "clothing"
description = "SCP is an artifact primarily intended to be worn for protection or comfort, including armor and protective helmets."

[[tags]]
name = "cognitohazard"
description = "SCP is hazardous to subjects when recorded by any of the traditional 5 senses."

[[tags]]
name = "compulsion"
description = "SCP induces compulsive behavior in subjects or otherwise causes subjects to do things they normally would not."

[[tags]]
name = "computer"
description = "SCP is a computational device or affects computational devices."

[[tags]]
name = "concept"
description = "SCP is or affects a purely non-physical concept. Should not be used in conjunction with tags describing physical qualities."

[[tags]]
name = "contagion"
description = "SCP is a contagious agent or exhibits contagious spread."

[[tags]]
name = "container"
description = "SCP is meant to hold or otherwise contain other material or objects, including decorative vases and other similar objects."

[[tags]]
name = "corporate"
description = "SCP affects the operations of a business or corporation."

[[tags]]
name = "corrosive"
description = "SCP exhibits corrosive properties."

[[tags]]
name = "currency"
description = "SCP is, is related to, affects, or is activated by money or other objects primarily intended to be used as a medium of exchange."

[[tags]]
name = "crystalline"
description = "SCP is or exhibits traits of crystals."

[[tags]]
name = "cube"
description = "SCP is cubical. Should only be used where the entire SCP is cubical or composed of cubes, rather than SCPs in which only one or more components are cubical."

[[tags]]
name = "dental"
description = "SCP is or deals with teeth or the practice of dentistry."

[[tags]]
name = "dinosaurian"
description = "SCP is or relates to a non-avian dinosaur."

[[tags]]
name = "document"
description = "SCP is a textual document of some sort. Includes books."

[[tags]]
name = "ectoentropic"
description = "SCP violates the first and/or second law of thermodynamics by generating matter and/or energy in a fashion that directly violates entropy."

[[tags]]
name = "electrical"
description = "SCP generates, stores, or uses electric energy."

[[tags]]
name = "electromagnetic"
description = "SCP generates, stores, or uses electromagnetic energy or fields."

[[tags]]
name = "electronic"
description = "SCP is or resembles an electronic device."

[[tags]]
name = "empathic"
description = "SCP is capable of reading or conveying emotion, feelings, or sensations."

[[tags]]
name = "engraved"
description = "SCP is or has carvings and/or engravings."

[[tags]]
name = "entropic"
description = "SCP is, exhibits traits of, or is related to entropy or entropic decay."

[[tags]]
name = "equine"
description = "SCP is or exhibits traits of equine or horse-like animals."

[[tags]]
name = "exchange"
description = "SCP involves or is triggered by some form of exchange of physical or intangible goods, including but not limited to bartering and monetary trade."

[[tags]]
name = "extradimensional"
description = "SCP is of extradimensional origin, moves or propagates extradimensionally, and/or enables extradimensional travel."

[[tags]]
name = "extraterrestrial"
description = "SCP originates or is found in outer space and/or enables or exhibits extraterrestrial travel."

[[tags]]
name = "extremity"
description = "SCP is or affects specific extremities, regardless of species."

[[tags]]
name = "feline"
description = "SCP is or is related to feline or cat-like animals."

[[tags]]
name = "fire"
description = "SCP is composed of fire, is related to fire, or enables the process of combustion."

[[tags]]
name = "food"
description = "SCP is primarily intended to be an edible object or substance."

[[tags]]
name = "foundation-made"
description = "SCP was created, intentionally or otherwise, by the SCP Foundation itself."

[[tags]]
name = "fungus"
description = "SCP is or exhibits traits of fungal life-forms."

[[tags]]
name = "furniture"
description = "SCP is or resembles a piece of furniture."

[[tags]]
name = "future"
description = "SCP is from the future or was otherwise temporally displaced from a later time frame into an earlier one."

[[tags]]
name = "game"
description = "SCP is, is used in, is activated by, or is otherwise related to one or more games, defined as a method of play or a sport -- especially a competitive one -- that can be won or lost by skill, strength, or luck."

[[tags]]
name = "gaseous"
description = "SCP is or generates a gas."

[[tags]]
name = "genetic"
description = "SCP is related to or functions primarily via genetic encoding and decoding."

[[tags]]
name = "geological"
description = "SCP is or affects natural geological formations (such as caves, cliffs, mountains, valleys, or volcanoes) or significant geological events (such as earthquakes, landslides, or sinkholes)."

[[tags]]
name = "glass"
description = "SCP is primarily or significantly composed of glass."

[[tags]]
name = "gravity"
description = "SCP affects or is significantly affected by gravitational force."

[[tags]]
name = "gustatory"
description = "SCP is triggered by, activated by, or affects the sense of taste."

[[tags]]
name = "hallucination"
description = "SCP induces hallucinations in subjects or is a hallucination."

[[tags]]
name = "historical"
description = "SCP affects or is prominent in historical events or has historical significance."

[[tags]]
name = "hive-mind"
description = "SCP exhibits traits of an external hive-mind."

[[tags]]
name = "hostile"
description = "SCP exhibits directed hostility towards personnel or subjects above and beyond that of instinctual or predatory behavior."

[[tags]]
name = "humanoid"
description = "SCP is humanoid or exhibits traits of humanoids."

[[tags]]
name = "immobile"
description = "SCP cannot be moved via any means known by the Foundation."

[[tags]]
name = "indestructible"
description = "SCP cannot be destroyed via any means known by the Foundation."

[[tags]]
name = "infohazard"
description = "SCP has an effect that is triggered when it is described or referred to."

[[tags]]
name = "insect"
description = "SCP is or is related to insects. This does not includes spiders."

[[tags]]
name = "inscribed"
description = "SCP has inscriptions on it, usually in the form of words or numbers."

[[tags]]
name = "inscription"
description = "SCP is an inscription, meaning it takes the form of written or carved words or numbers."

[[tags]]
name = "instrument"
description = "SCP is an instrument or a tool intended for either delicate, scientific, or measuring work."

[[tags]]
name = "intangible"
description = "SCP is intangible in a manner that precludes definition as a gas."

[[tags]]
name = "invertebrate"
description = "SCP exhibits traits of invertebrates or animals lacking spinal columns."

[[tags]]
name = "jewelry"
description = "SCP is an object primarily intended to be worn in a decorative manner."

[[tags]]
name = "k-class-scenario"
description = "SCP is involved in or capable of instigating one or more K-Class End of the World scenarios."

[[tags]]
name = "key"
description = "SCP is a standard key or otherwise intended to unlock one or more devices or containers."

[[tags]]
name = "knowledge"
description = "SCP absorbs, stores, generates, grants, or possesses knowledge that is anomalous, or through an anomalous process."

[[tags]]
name = "language"
description = "SCP imparts, exhibits, or is an anomalous language."

[[tags]]
name = "lepidopteran"
description = "SCP is or exhibits traits of lepidopteran or butterfly-, moth-, or skipper-like animals."

[[tags]]
name = "leporine"
description = "SCP is or exhibits traits of leporine or rabbit- or hare-like animals."

[[tags]]
name = "light"
description = "SCP is triggered, activated, or propagated by or otherwise related to the presence or absence of visible light."

[[tags]]
name = "liquid"
description = "SCP is or generates a liquid."

[[tags]]
name = "location"
description = "SCP is a unique geographical location."

[[tags]]
name = "loop"
description = "SCP exhibits or is engaged in a repeating loop of activity."

[[tags]]
name = "magnetic"
description = "SCP is magnetic or exhibits traits of magnetic charge and/or attraction."

[[tags]]
name = "map"
description = "SCP is a map, has a map, or otherwise exhibits visual representations in the manner of a map."

[[tags]]
name = "mathematical"
description = "SCP is or affects a number, number system, mathematical equation, or otherwise has mathematical significance."

[[tags]]
name = "mechanical"
description = "SCP operates primarily in a mechanical manner or is a mechanical device."

[[tags]]
name = "media"
description = "SCP is or is contained on, one or more items of fixed or removable analog or digital media, such as a tape, record, disc, or drive."

[[tags]]
name = "medical"
description = "SCP is used or intended for use as a medical device or otherwise has medical significance outside of pathology."

[[tags]]
name = "memetic"
description = "SCP is a memetic agent or exhibits traits of memetic propagation."

[[tags]]
name = "memory-affecting"
description = "SCP imparts, changes, or removes memories in sentient beings such as human subjects."

[[tags]]
name = "meta"
description = "SCP affects or is affected by its documentation or requires containment procedures regarding the way it is documented."

[[tags]]
name = "metallic"
description = "SCP is a metal or is completely or significantly composed of metal or metallic substances."

[[tags]]
name = "metamorphic"
description = "SCP changes its form or shape, often to mimic the form or shape of other objects or entities. Often used to describe shapeshifters or mimics."

[[tags]]
name = "meteorological"
description = "SCP is, affects, or is affected by significant weather elements."

[[tags]]
name = "microscopic"
description = "SCP is too small to be seen or otherwise meaningfully observed by the naked eye."

[[tags]]
name = "military"
description = "SCP is military equipment, part or member of a military unit, or otherwise has military significance."

[[tags]]
name = "mimetic"
description = "SCP exhibits anomalous mimicry."

[[tags]]
name = "mind-affecting"
description = "SCP affects the thinking of subjects, which can include behavior and overall intelligence."

[[tags]]
name = "miniature"
description = "SCP is much smaller than objects it resembles."

[[tags]]
name = "mobile"
description = "SCP is capable of movement by anomalous means. Generally only applies to objects or entities that are normally incapable of movement."

[[tags]]
name = "moon"
description = "SCP is, is related to, or affects a natural satellite or moon, which may or may not be our moon."

[[tags]]
name = "murine"
description = "SCP is or exhibits traits of murine, or mouse-like or rat-like animals."

[[tags]]
name = "musical"
description = "SCP is, generates, or is generated by musical compositions."

[[tags]]
name = "narrative"
description = "SCP is, is related to, or propagates via narrative information or documents."

[[tags]]
name = "neurological"
description = "SCP directly or indirectly affects the neurological system of subjects."

[[tags]]
name = "nocturnal"
description = "SCP is triggered by, activated by, or otherwise is only significantly active at night."

[[tags]]
name = "observational"
description = "SCP has properties that are triggered or suppressed when directly or indirectly observed."

[[tags]]
name = "ocular"
description = "SCP resembles, is related to, or affects eyes."

[[tags]]
name = "olfactory"
description = "SCP exhibits anomalous scent, is propagated through smell, or affects the sense of smelling."

[[tags]]
name = "omnivorous"
description = "SCP exhibits omnivorous traits."

[[tags]]
name = "online"
description = "SCP is available on, utilizes, or is dependent on a connection to the internet."

[[tags]]
name = "ontokinetic"
description = "SCP is capable of manipulating reality (aka 'reality-bending') through anomalous means."

[[tags]]
name = "ophidian"
description = "SCP is or exhibits traits of ophidian, or snake-like animals."

[[tags]]
name = "organic"
description = "SCP exhibits organic traits or composition."

[[tags]]
name = "paradox"
description = "SCP generates, exhibits, or is involved in paradoxical events or situations."

[[tags]]
name = "parasitic"
description = "SCP exhibits traits of parasitic or parasitoid organisms."

[[tags]]
name = "performance"
description = "SCP is or is used in a performance art, such as a dance or play."

[[tags]]
name = "physics"
description = "SCP affects or violates particular physical laws."

[[tags]]
name = "photographic"
description = "SCP is or deals with photography or features a photograph as part of the primary anomaly."

[[tags]]
name = "piscine"
description = "SCP is or exhibits traits of piscine or fish-like animals."

[[tags]]
name = "plant"
description = "SCP is a plant or exhibits plant-like traits."

[[tags]]
name = "planet"
description = "SCP is, resembles, or affects a planet, which may or may not be our planet."

[[tags]]
name = "polyhedral"
description = "SCP is a polyhedron: a three-dimensional shape with flat faces and straight edges."

[[tags]]
name = "portal"
description = "SCP is an opening or doorway that exhibits inconsistent connectivity."

[[tags]]
name = "predatory"
description = "SCP exhibits predatory behavior."

[[tags]]
name = "predictive"
description = "SCP is capable of imparting information or acting in a predictive manner."

[[tags]]
name = "probability"
description = "SCP alters or manipulates the probability of certain events or outcomes."

[[tags]]
name = "radioactive"
description = "SCP emits radiation or affects radioactivity."

[[tags]]
name = "ranine"
description = "SCP is or exhibits traits of ranine or frog-like animals."

[[tags]]
name = "reanimation"
description = "SCP has been restored or restores others, either whole or in part, to life from a clinically dead state."

[[tags]]
name = "recording"
description = "SCP is or contains an audio and/or visual recording."

[[tags]]
name = "religious"
description = "SCP is associated with or otherwise has significance to one or more organized religions."

[[tags]]
name = "reproductive"
description = "SCP anomalously affects or interferes with the normal biological reproductive processes of an organism (which may include humans), or has anomalous biological reproductive methods."

[[tags]]
name = "reptilian"
description = "SCP is or exhibits traits of reptilian or reptile-like animals."

[[tags]]
name = "ritual"
description = "SCP is or is triggered or activated through ritualistic behavior."

[[tags]]
name = "sapient"
description = "SCP exhibits sapient traits, such as the ability to grasp philosophical concepts."

[[tags]]
name = "satellite"
description = "SCP is a natural or artificial satellite orbiting a celestial body."

[[tags]]
name = "sciurine"
description = "SCP is or exhibits traits of sciurine or squirrel-like animals."

[[tags]]
name = "sculpture"
description = "SCP is a three-dimensional piece of artwork, having been formed, carved, or molded."

[[tags]]
name = "selachian"
description = "SCP is or exhibits traits of selacian or shark-like animals. Also includes rays and skates."

[[tags]]
name = "self-repairing"
description = "SCP exhibits an anomalous ability restore or repair itself to functional condition."

[[tags]]
name = "self-replicating"
description = "SCP exhibits an anomalous ability to replicate other than via biological reproduction."

[[tags]]
name = "sensory"
description = "SCP affects sensory perception."

[[tags]]
name = "sexual"
description = "SCP includes or affects sexual organs, sexual activities, or concepts related to sex. Does not imply that the work is intended for adult audiences only."

[[tags]]
name = "sentient"
description = "SCP exhibits sentient traits, such as self-awareness and cognitive deduction."

[[tags]]
name = "shadow"
description = "SCP is triggered, activated, or otherwise significantly affected by shadows cast by subjects."

[[tags]]
name = "simian"
description = "SCP is or exhibits traits of simian, or ape-like animals."

[[tags]]
name = "skeletal"
description = "SCP is, is a component of, or affects the skeletal tissue of an organism. A skeleton is the structural support tissue of a multi-celled organism, and includes both bones and cartilage."

[[tags]]
name = "sleep"
description = "SCP is related to sleep."

[[tags]]
name = "spacetime"
description = "SCP warps space-time or affects or violates laws of space-time."

[[tags]]
name = "species"
description = "SCP describes an entire species, rather than one or more individuals."

[[tags]]
name = "sphere"
description = "SCP is spherical."

[[tags]]
name = "sport"
description = "SCP is, is used in, is activated by, or is otherwise related to one or more sports, defined as an activity involving physical exertion and skill in which one or more individuals compete against other individuals or teams."

[[tags]]
name = "statue"
description = "SCP is or was a statue. A statue is defined as a free-standing, full-body sculpture of a person or animal."

[[tags]]
name = "stone"
description = "SCP is composed primarily of stone (meaning concreted earthy or mineral matter) or rock."

[[tags]]
name = "structure"
description = "SCP is an artificial or natural structure; if it is intended for human occupation, it should be tagged building instead."

[[tags]]
name = "subterranean"
description = "SCP is located or operates wholly or significantly underground, defined as below the surface of the Earth. Does not apply objects that are simply contained underground for safety or convenience."

[[tags]]
name = "sun"
description = "SCP is, is related to, or affects a sun, which may or may not be our sun."

[[tags]]
name = "swarm"
description = "SCP exhibits swarm behavior."

[[tags]]
name = "tactile"
description = "SCP is activated by, triggered by, or affects the sense of touch. Note that this refers specifically to the sense of touch, not simply something that can activate by touching something else."

[[tags]]
name = "telekinetic"
description = "SCP can manipulate objects or initiate or affect reactions through anomalous means."

[[tags]]
name = "telepathic"
description = "SCP can transfer information via anomalous means."

[[tags]]
name = "teleportation"
description = "SCP can move without occupying intervening space or otherwise displace itself via anomalous means that preclude normal movement."

[[tags]]
name = "temporal"
description = "SCP affects or is otherwise related to the passage of time."

[[tags]]
name = "thermal"
description = "SCP is activated by, triggered by, or propagates via changes in temperature. This includes both increases and decreases in temperature."

[[tags]]
name = "thermodynamic"
description = "SCP affects, or is otherwise significantly related to the laws of thermodynamics."

[[tags]]
name = "timepiece"
description = "SCP is, or a major component of, an instrument or mechanism designed to measure time."

[[tags]]
name = "tool"
description = "SCP is (or was intended to be) used as a tool."

[[tags]]
name = "toxic"
description = "SCP induces chemical toxicity in subjects."

[[tags]]
name = "toy"
description = "SCP is, or was primarily intended to be, used as a toy."

[[tags]]
name = "transfiguration"
description = "SCP alters the shape or substance of subjects in an anomalous manner."

[[tags]]
name = "transmission"
description = "SCP transmits information, typically via radio waves or other electromagnetic means."

[[tags]]
name = "uncontained"
description = "SCP is neither fully nor partially contained."

[[tags]]
name = "ursine"
description = "SCP is or exhibits traits of ursine, or bear-like animals."

[[tags]]
name = "vehicle"
description = "SCP is or is intended to be used as a vehicle."

[[tags]]
name = "vermian"
description = "SCP is or exhibits traits of vermian, or worm-like animals."

[[tags]]
name = "vibration"
description = "SCP generates anomalous vibrations or other repetitive movement."

[[tags]]
name = "virus"
description = "SCP exhibits traits of viral agents."

[[tags]]
name = "visual"
description = "SCP is triggered by, activated by, or affects the sense of sight."

[[tags]]
name = "weapon"
description = "SCP is or is intended to be used as a weapon."

[[tags]]
name = "wooden"
description = "SCP is composed primarily or significantly of wood or wood-like material."

[[tags]]
name = "abnormalities"
description = "Of of related to the Department of Abnormalities."

[[tags]]
name = "accelerate-the-future"
description = "Of or related to Accelerate the Future."

[[tags]]
name = "alexylva"
description = "Of or related to the Alexylva University group of interest."

[[tags]]
name = "ambrose-restaurant"
description = "Of or related to the Ambrose Restaurant."

[[tags]]
name = "anderson"
description = "Of or related to the Anderson Robotics group of interest."

[[tags]]
name = "arcadia"
description = "Of or related to the Arcadia organization."

[[tags]]
name = "are-we-cool-yet"
description = "Of or related to the Are We Cool Yet? (AWCY) group of interest."

[[tags]]
name = "asci"
description = "Of or related to the American Secure Containment Initiative."

[[tags]]
name = "avelar"
description = "Of or related to Avelar Professional Products."

[[tags]]
name = "black-queen"
description = "Of or related to the Black Queen group of interest."

[[tags]]
name = "blackwood"
description = "Of or related to The Adventures of Lord Blackwood, Explorer and Gentleman."

[[tags]]
name = "british-occult-service"
description = "Of or related to the British Occult Service (MI666) group of interest."

[[tags]]
name = "broken-god"
description = "Of or related to Mekhane, or the Church of the Broken God (CotBG) group of interest."

[[tags]]
name = "brothers-of-death"
description = "Of or related to the Brothers of Death canon or characers."

[[tags]]
name = "chaos-insurgency"
description = "Of or related to the Chaos Insurgency (CI) group of interest."

[[tags]]
name = "chicago-spirit"
description = "Of or related to the Chicago Spirit group of interest."

[[tags]]
name = "children-of-the-night"
description = "Of or related to the Children of the Night, outlined in SCP-1000."

[[tags]]
name = "children-of-the-torch"
description = "SCP is of or related to the Children of the Torch group of Interest."

[[tags]]
name = "class-of-76"
description = "Of or related to the Class of '76 SCPs and stories."

[[tags]]
name = "daevite"
description = "Of or related to the Daevites."

[[tags]]
name = "decommissioning-dept"
description = "Of or related to the Decommissioning Department."

[[tags]]
name = "deer-college"
description = "Of or related to the Deer College group of interest."

[[tags]]
name = "dr-wondertainment"
description = "Of or related to the Dr. Wondertainment individual or group of interest."

[[tags]]
name = "ethics-committee"
description = "Of or related to the Foundation Ethics Committee."

[[tags]]
name = "factory"
description = "Of or related to The Factory group of interest."

[[tags]]
name = "fifthist"
description = "Of or related to The Fifthist Church group of interest."

[[tags]]
name = "folklore-dept"
description = "Of or related to the Foundation Department of Mythology and Folkloristics."

[[tags]]
name = "gamers-against-weed"
description = "Of or related to The Gamers Against Weed group of interest."

[[tags]]
name = "global-occult-coalition"
description = "Of or related to the Global Occult Coalition (GOC) group of interest."

[[tags]]
name = "golden-horde"
description = "Of or related to the Golden Horde group of interest."

[[tags]]
name = "greazeburger"
description = "Of or related to the Greazeburger group of interest."

[[tags]]
name = "gru-division-p"
description = "Of or related to the GRU Division \"P\" group of interest."

[[tags]]
name = "herman-fuller"
description = "Of or related to the Herman Fuller's Circus of the Disquieting group of interest."

[[tags]]
name = "hmfscp"
description = "Of or related to His/Her Majesty's Foundation For The Study of Curiosities and Phantasmagoria."

[[tags]]
name = "horizon-initiative"
description = "Of or related to the Horizon Initiative group of interest."

[[tags]]
name = "icsut"
description = "Of or related to the International Center for the Study of Unified Thaumatology."

[[tags]]
name = "ijamea"
description = "Of or related to the Imperial Japanese Anomalous Matters Examination Agency."

[[tags]]
name = "madao"
description = "Of or related to the Italian GoI Medicean Academy of Occult Art (Medicea Accademia Dell'Arte Occulta)."

[[tags]]
name = "mages-academy"
description = "Of or related to the Mages Academy group of interest."

[[tags]]
name = "manna-charitable-foundation"
description = "Of or related to the Manna Charitable Foundation group of interest."

[[tags]]
name = "marshall-carter-and-dark"
description = "Of or related to the Marshall, Carter, and Dark Ltd. (MC&D) group of interest."

[[tags]]
name = "miscommunications"
description = "Of or related to the Department of Miscommunications."

[[tags]]
name = "nameless"
description = "Of or related to the Nameless, or the Fae, outlined in SCP-4000."

[[tags]]
name = "nobody"
description = "Of or related to the 'Nobody' group of interest."

[[tags]]
name = "obearwatch"
description = "Of or related to the Obearwatch group of interest."

[[tags]]
name = "obskura"
description = "Of or related to the Obskura Corps group of interest."

[[tags]]
name = "oneiroi"
description = "Of or related to the Oneiroi Collective group of interest."

[[tags]]
name = "parawatch"
description = "Of or related to the Parawatch Wiki."

[[tags]]
name = "pattern-screamer"
description = "Of or related to pattern screamers."

[[tags]]
name = "pentagram"
description = "Of or related to Pentagram."

[[tags]]
name = "professor-aw"
description = "Of or related to the inventions and curiosities of one Professor A. W."

[[tags]]
name = "prometheus"
description = "Of or related to the Prometheus Labs group of interest."

[[tags]]
name = "reclamation"
description = "Of or related to the Office For The Reclamation of Islamic Artifacts (ORIA) group of interest. ."

[[tags]]
name = "sapphire"
description = "Of or related to the SAPPHIRE group of interest. ."

[[tags]]
name = "sarkic"
description = "Of or related to the Sarkic Cults group of interest."

[[tags]]
name = "second-hytoth"
description = "Of or related to the Church of the Second Hytoth group of Interest."

[[tags]]
name = "serpents-hand"
description = "Of or related to the Serpent's Hand group of interest."

[[tags]]
name = "shark-punching-center"
description = "Of or related to the Shark Punching Center."

[[tags]]
name = "silicon-nornir"
description = "Of or related to the Servants of the Silicon Nornir religion."

[[tags]]
name = "sugarcomb-confectionery"
description = "Of or related to Sugarcomb Confectionery."

[[tags]]
name = "surrealistics-dept"
description = "Of or related to the Foundation Department of Surrealistics."

[[tags]]
name = "tactical-theology"
description = "Of or related to the Department of Tactical Theology."

[[tags]]
name = "telecom-office"
description = "Of or related to the Foundation Telecommunications Monitoring Office."

[[tags]]
name = "three-moons-initiative"
description = "Of or related to the Three Moons Initiative."

[[tags]]
name = "totleighsoft"
description = "Of or related to the anomalous software development corporation TotleighSoft."

[[tags]]
name = "unusual-cargo"
description = "Of or related to the Commission on Unusual Cargo."

[[tags]]
name = "unusual-incidents-unit"
description = "Of or related to the Federal Bureau of Investigation Unusual Incidents Unit (UIU) group of interest."

[[tags]]
name = "vikander-kneed"
description = "Of or related to the Vikander-Kneed Technical Media group of interest."

[[tags]]
name = "wandsmen"
description = "Of of related to the Wandsmen group of interest."

[[tags]]
name = "westhead-media"
description = "Of or related to the Westhead Media group of interest."

[[tags]]
name = "wilsons-wildlife"
description = "Of or related to the Wilson's Wildlife organization."

[[tags]]
name = "xia-dynasty"
description = "Of or related to the Xia Dynasty."

[[tags]]
name = "_alexylva"
description = "An article following the Alexylva Universiy format."

[[tags]]
name = "_ambrose-restaurant"
description = "An article following the Ambrose Restaurants format."

[[tags]]
name = "_anderson"
description = "An article following the Anderson Robotics format."

[[tags]]
name = "_arcadia"
description = "An article following the Arcadia format."

[[tags]]
name = "_are-we-cool-yet"
description = "An article following the Are We Cool Yet? format."

[[tags]]
name = "_black-queen"
description = "An article following the Black Queen format."

[[tags]]
name = "_broken-god"
description = "An article following the Church of the Broken God format."

[[tags]]
name = "_chaos-insurgency"
description = "An article following the Chaos Insurgency format."

[[tags]]
name = "_chicago-spirit"
description = "An article following the Chicago Spirit format."

[[tags]]
name = "_deer-college"
description = "An article following the Deer College format."

[[tags]]
name = "_eric"
description = "An article following the Eric format."

[[tags]]
name = "_factory"
description = "An article following the Factory format."

[[tags]]
name = "_fifthist"
description = "An article following the Fifthist format."

[[tags]]
name = "_global-occult-coalition"
description = "An article following the Global Occult Coalition format."

[[tags]]
name = "_gru-division-p"
description = "An article following the GRU Division P format."

[[tags]]
name = "_herman-fuller"
description = "An article following the Herman Fuller format."

[[tags]]
name = "_horizon-initiative"
description = "An article following the Horizon Initiative format."

[[tags]]
name = "_icsut"
description = "An article following the International Center for the Study of Unified Thaumatology."

[[tags]]
name = "_ijamea"
description = "An article following the IJAMEA format."

[[tags]]
name = "_la-rue-macabre"
description = "An article following the La Rue Macabre format."

[[tags]]
name = "_madao"
description = "An article following the Medicea Accademia format."

[[tags]]
name = "_manna-charitable-foundation"
description = "An article following the Manna Charitable Foundation format."

[[tags]]
name = "_marshall-carter-and-dark"
description = "An article following the Marshall, Carter and Dark format."

[[tags]]
name = "_nobody"
description = "An article following the Nobody format."

[[tags]]
name = "_oneiroi"
description = "An article following the Oneiroi format."

[[tags]]
name = "_other"
description = "A GoI Format following a format not associated with a tagged Group of Interest."

[[tags]]
name = "_prometheus"
description = "An article following the Prometheus format."

[[tags]]
name = "_reclamation"
description = "An article following the Reclamation format."

[[tags]]
name = "_sapphire"
description = "An article following the SAPPHIRE format."

[[tags]]
name = "_sarkic"
description = "An article following the Sarkic format."

[[tags]]
name = "_second-hytoth"
description = "An article following the Second Hytoth format."

[[tags]]
name = "_serpents-hand"
description = "An article following the Serpents' Hand format."

[[tags]]
name = "_shark-punching-center"
description = "An article following the Shark Punching Center format."

[[tags]]
name = "_three-moons-initiative"
description = "An article following the Three Moons Initiative format."

[[tags]]
name = "_unusual-cargo"
description = "An article following the Unusual Cargo format."

[[tags]]
name = "_unusual-incidents-unit"
description = "An article following the Unusual Incidents Unit format."

[[tags]]
name = "_wandsmen"
description = "An article following the Wandsmen format."

[[tags]]
name = "_wilsons-wildlife"
description = "An article following the Wilsons' Wildlife format."

[[tags]]
name = "aces-and-eights"
description = "Of or related to the Aces and Eights canon."

[[tags]]
name = "aiad"
description = "Of or related to the AIAD canon."

[[tags]]
name = "ad-astra"
description = "Of or related to the Ad Astra Per Aspera canon."

[[tags]]
name = "alchemy-department"
description = "Of or related to The Alchemy Department canon."

[[tags]]
name = "antarctic-exchange"
description = "Of or related to the Antarctic Exchange canon."

[[tags]]
name = "apotheosis"
description = "Of or related to the Apotheosis canon."

[[tags]]
name = "bellerverse"
description = "Of or related to the Bellerverse canon."

[[tags]]
name = "black-rabbit-company"
description = "Of or related to the Stealing Solidarity canon."

[[tags]]
name = "broken-masquerade"
description = "Of or related to the Broken Masquerade canon."

[[tags]]
name = "competitive-eschatology"
description = "Of or related to the Competitive Eschatology canon."

[[tags]]
name = "cool-war-2"
description = "Of or related to the Cool War 2: Ruiz From Your Grave canon."

[[tags]]
name = "daybreak"
description = "Of or related to the Daybreak canon."

[[tags]]
name = "deepwell-catalog"
description = "Of or related to the Site-17 Deepwell canon."

[[tags]]
name = "doctors-of-the-church"
description = "Of or related to the Doctors of the Church canon."

[[tags]]
name = "dread&circuses"
description = "Of or related to the Dread and Circuses canon."

[[tags]]
name = "end-of-death"
description = "Of or related to the End of Death canon."

[[tags]]
name = "etdp"
description = "Of or related to the Et Tam Deum Petivi canon."

[[tags]]
name = "from-120s-archives"
description = "Of or related to the From 120's Archives canon."

[[tags]]
name = "green-king"
description = "Of or related to the Codename: Green King hub."

[[tags]]
name = "heimdall"
description = "Of or related to Project Heimdall."

[[tags]]
name = "insect-hell"
description = "Of or related to the Insect Hell canon."

[[tags]]
name = "lolfoundation"
description = "Of or related to the lolFoundation canon."

[[tags]]
name = "man-who-wasnt-there"
description = "Of or relating to The Man Who Wasn't There canon."

[[tags]]
name = "memoria-adytum"
description = "Of or related to the In Memoria, Adytum canon."

[[tags]]
name = "no-return"
description = "Of or related to the No Return canon."

[[tags]]
name = "old-man-in-the-sea"
description = "Of or related to the Old Man in the Sea canon."

[[tags]]
name = "on-guard-43"
description = "Of or related to the On Guard 43 canon."

[[tags]]
name = "on-mount-golgotha"
description = "Of or related to the On Mount Golgotha canon."

[[tags]]
name = "only-game-in-town"
description = "Of or related to the Only Game in Town canon."

[[tags]]
name = "orcadia"
description = "Of or related to the Seas of Orcadia canon."

[[tags]]
name = "pitch-haven"
description = "Of or related to the Pitch Haven canon."

[[tags]]
name = "rats-nest"
description = "Of or related to the Rat's Nest canon."

[[tags]]
name = "resurrection"
description = "Of or related to the Resurrection project."

[[tags]]
name = "s&c-plastics"
description = "Of or related to the S & C Plastics canon."

[[tags]]
name = "ship-in-a-bottle"
description = "Of or related to the Ship In A Bottle canon."

[[tags]]
name = "sotm"
description = "Of or related to the Straight On Till Morning canon."

[[tags]]
name = "the-coldest-war"
description = "Of or related to the Coldest War canon."

[[tags]]
name = "the-gulf"
description = "Of or related to The Gulf canon."

[[tags]]
name = "the-trashfire"
description = "Of or relating to The Trashfire canon."

[[tags]]
name = "third-law"
description = "Of or pertaining to the Third Law canon."

[[tags]]
name = "twisted-pines"
description = "Of or related to the Those Twisted Pines canon."

[[tags]]
name = "unfounded"
description = "Of or related to the Unfounded canon."

[[tags]]
name = "unhuman"
description = "Of or related to the UnHuman canon."

[[tags]]
name = "war-on-all-fronts"
description = "Of or related to the War On All Fronts canon."

[[tags]]
name = "wonderful-world"
description = "Of or related to the What a Wonderful World canon."

[[tags]]
name = "anabasis"
description = "Of or related to the Anabasis stories."

[[tags]]
name = "ao-tale"
description = "Articles based on an anomalous object."

[[tags]]
name = "classical-revival"
description = "Of or related to the Classical Revival stories."

[[tags]]
name = "collector-tale"
description = "Of or related to the Tales of Mr. Collector."

[[tags]]
name = "goc-casefiles"
description = "Of or related to the Global Occult Coalition Casefiles stories."

[[tags]]
name = "kiryu-labs"
description = "Of or related to the Kiryu Labs series."

[[tags]]
name = "mister"
description = "Of or related to the \"Little Misters\" series of anomalous individuals."

[[tags]]
name = "olympia"
description = "Of or related to the Olympia Project."

[[tags]]
name = "orientation"
description = "Of or related to the Orientation series."

[[tags]]
name = "palisade"
description = "Of the Project Palisade series."

[[tags]]
name = "project-crossover"
description = "Of or related to Project Crossover."

[[tags]]
name = "project-thaumiel"
description = "Of or related to Project Thaumiel."

[[tags]]
name = "team-bird"
description = "Of or related to Team Bird."

[[tags]]
name = "8-ball"
description = "8-ball, aka 8B-A1."

[[tags]]
name = "aaron-siegel"
description = "Aaron Siegel."

[[tags]]
name = "able"
description = "Able, aka SCP-076."

[[tags]]
name = "agent-green"
description = "Agent Green."

[[tags]]
name = "agent-kazmarek"
description = "Agent Travis Kazmarek."

[[tags]]
name = "agent-laferrier"
description = "Agent V.A. LaFerrier."

[[tags]]
name = "agent-lament"
description = "Agent Troy Lament."

[[tags]]
name = "agent-lurk"
description = "Agent Dietrich M. Lurk."

[[tags]]
name = "agent-merlo"
description = "Agent Sasha Merlo."

[[tags]]
name = "agent-navarro"
description = "Agent Daniel Navarro."

[[tags]]
name = "agent-popescu"
description = "Agent Lucretia Popescu."

[[tags]]
name = "agent-strelnikov"
description = "Agent Dmitri Strelnikov."

[[tags]]
name = "agent-trauss"
description = "Agent Trauss, aka C-51174."

[[tags]]
name = "agent-yoric"
description = "Agent Yoric Elroy, aka Jack \"Poor Yoric\" Dawkins."

[[tags]]
name = "aldon"
description = "Aldon."

[[tags]]
name = "alexandra"
description = "Alexandra, AI unit."

[[tags]]
name = "alexei-belitrov"
description = "Alexei Belitrov, aka SCP-2273."

[[tags]]
name = "alleged-god"
description = "SCP-343, aka \"God\"."

[[tags]]
name = "bailey-brothers"
description = "Tristan, Thomas and Trevor Bailey."

[[tags]]
name = "big-cheese-horace"
description = "Big Cheese Horace of the Fifthists."

[[tags]]
name = "bobble-the-clown"
description = "Bobble The Clown, aka SCP-993."

[[tags]]
name = "bones"
description = "Bones, aka SCP-2721-LORD or Eli."

[[tags]]
name = "brainy-brian"
description = "Brainy Brian of Wondertainment/MC&D, also known as 'Doctor Neurosis'."

[[tags]]
name = "cain"
description = "Cain, aka SCP-073."

[[tags]]
name = "chaz-ambrose"
description = "Chaz Ambrose, founder of Ambrose Restaurants."

[[tags]]
name = "cousin-johnny"
description = "Cousin Johnny, aka SCP-2852."

[[tags]]
name = "d-7294"
description = "D-7294."

[[tags]]
name = "d-11424"
description = "D-11424."

[[tags]]
name = "dado"
description = "dado is taking care of u in dis one. u no worry."

[[tags]]
name = "dc-al-fine"
description = "D.C. al Fine, Undersecretary-General of the Global Occult Coalition."

[[tags]]
name = "director-aktus"
description = "Director Aktus."

[[tags]]
name = "director-bold"
description = "Director Cal Bold of the Decommissioning Department."

[[tags]]
name = "director-diaghilev"
description = "Director Ruslav Diaghilev of the Alchemy Department."

[[tags]]
name = "director-gillespie"
description = "Director Gillespie."

[[tags]]
name = "director-mcinnis"
description = "Dr. Allan J. McInnis, Director of Site-43."

[[tags]]
name = "director-mctiriss"
description = "Director Kate McTiriss."

[[tags]]
name = "director-moose"
description = "Director Moose."

[[tags]]
name = "director-lague"
description = "Director Paul Lague, of the Integration Program and Site-322."

[[tags]]
name = "django-bridge"
description = "Django Bridge."

[[tags]]
name = "doctor-asheworth"
description = "Dr. Daniel Asheworth."

[[tags]]
name = "doctor-blank"
description = "Dr. Harold R. Blank."

[[tags]]
name = "doctor-bright"
description = "Dr. Bright."

[[tags]]
name = "doctor-cimmerian"
description = "Dr. Cimmerian."

[[tags]]
name = "doctor-clef"
description = "Dr. Alto Clef."

[[tags]]
name = "doctor-dan"
description = "Dr. Dan ███████, of SCP-096."

[[tags]]
name = "doctor-edison"
description = "Dr. Michael Edison."

[[tags]]
name = "doctor-elliott"
description = "Dr. Chelsea Elliott."

[[tags]]
name = "doctor-everwood"
description = "Dr. Everwood, GOI specialist."

[[tags]]
name = "doctor-fynegan"
description = "Dr. Fynegan."

[[tags]]
name = "doctor-gears"
description = "Dr. Gears."

[[tags]]
name = "doctor-gerald"
description = "Dr. Gerald."

[[tags]]
name = "doctor-glass"
description = "Dr. Simon Glass."

[[tags]]
name = "doctor-heiden"
description = "Dr. Frederick Heiden."

[[tags]]
name = "doctor-hoygull"
description = "Dr. Hoygull, Avian Division."

[[tags]]
name = "doctor-iceberg"
description = "Dr. Iceberg."

[[tags]]
name = "doctor-king"
description = "Dr. King."

[[tags]]
name = "doctor-kondraki"
description = "Dr. Kondraki."

[[tags]]
name = "doctor-light"
description = "Dr. Sophia N. Light."

[[tags]]
name = "doctor-lillihammer"
description = "Dr. Lillian S. Lillihammer."

[[tags]]
name = "doctor-mann"
description = "Dr. Everett Mann."

[[tags]]
name = "doctor-mcdoctorate"
description = "Dr. Placeholder McDoctorate."

[[tags]]
name = "doctor-reynders"
description = "Dr. Ilse Reynders."

[[tags]]
name = "doctor-rights"
description = "Dr. Rights."

[[tags]]
name = "doctor-rivera"
description = "Dr. Jessie Rivera."

[[tags]]
name = "doctor-roget"
description = "Dr. Ralph Roget."

[[tags]]
name = "doctor-thereven"
description = "Doctor Cole Thereven."

[[tags]]
name = "doctor-sinclair"
description = "Dr. Katherine Sinclair."

[[tags]]
name = "doctor-sorts"
description = "Dr. Johannes Sorts."

[[tags]]
name = "doctor-spanko"
description = "Dr. Spanko."

[[tags]]
name = "doctor-vang"
description = "Dr. S. Vang."

[[tags]]
name = "doctor-wettle"
description = "Dr. William Wallace Wettle."

[[tags]]
name = "donkman"
description = "Ulysses B. Donkman."

[[tags]]
name = "draven-kondraki"
description = "Dr./Director Draven Kondraki."

[[tags]]
name = "eric"
description = "Eric, a mysterious character."

[[tags]]
name = "esther-kogan"
description = "Esther Kogan, aka lesbian_gengar of Gamers Against Weed."

[[tags]]
name = "faeowynn-wilson"
description = "Faeowynn \"Fae\" Wilson."

[[tags]]
name = "finnegan"
description = "Finnegan."

[[tags]]
name = "fred"
description = "Fred, aka SCP-423."

[[tags]]
name = "general-bowe"
description = "General Bowe."

[[tags]]
name = "glacon"
description = "Glacon.aic."

[[tags]]
name = "grabnok"
description = "Grabnok the Destroyer, aka SCP-507."

[[tags]]
name = "grand-karcist-ion"
description = "Grand Karcist Ion, a Sarkic figure."

[[tags]]
name = "halyna-ieva"
description = "Karcist Halyna Ieva, aka The Mother Who Demands One's Toes."

[[tags]]
name = "hanged-king"
description = "Of or relating to the Hanged King."

[[tags]]
name = "hard-to-kill-reptile"
description = "The \"Hard-To-Destroy Reptile\", aka SCP-682."

[[tags]]
name = "heather-mason"
description = "Heather Mason, aka \"Ms. Mad About Video Games\" or SCP-3090."

[[tags]]
name = "holly-light"
description = "Holly Light."

[[tags]]
name = "icky"
description = "Veronica the Magic Clown."

[[tags]]
name = "iris-dark"
description = "Iris Dark."

[[tags]]
name = "iris-thompson"
description = "Iris Thompson, aka SCP-105."

[[tags]]
name = "isabel-v"
description = "Isabel Helga Anastasia Parvati Wondertainment V."

[[tags]]
name = "jockjamsvol6"
description = "JJ, AKA jockjamsvol6 of Gamers Against Weed."

[[tags]]
name = "jude-kriyot"
description = "Jude Kriyot, AKA bluntfiend of Gamers Against Weed."

[[tags]]
name = "judith-low"
description = "Dr. Judith Low, Department of History."

[[tags]]
name = "judy-papill"
description = "Judy Papill, AKA Judy the Tongue."

[[tags]]
name = "kain-pathos-crow"
description = "Professor Kain Pathos Crow."

[[tags]]
name = "kenneth-spencer"
description = "Kenneth Spencer."

[[tags]]
name = "kindness"
description = "A kind man."

[[tags]]
name = "legate-trunnion"
description = "Legate Trunnion, prophet of the Cogwork Orthodoxy."

[[tags]]
name = "leslie"
description = "Leslie, instance of SCP-3774."

[[tags]]
name = "lewitt-zairi-family"
description = "The Lewitt Zairi Family."

[[tags]]
name = "lombardi"
description = "Agent Lombardi."

[[tags]]
name = "manny"
description = "Manny, aka The Man With the Upside Down Face of Herman Fuller."

[[tags]]
name = "maria-jones"
description = "Maria Jones of RAISA."

[[tags]]
name = "marion-wheeler"
description = "Marion Wheeler."

[[tags]]
name = "mark-kiryu"
description = "Mark Kiryu of Kiryu Labs."

[[tags]]
name = "moon-champion"
description = "Moon Champion, aka Champion of the Moon or SCP-1233."

[[tags]]
name = "mr-fish"
description = "Mr. Fish, Little Mister from Dr. Wondertainment and SCP-527."

[[tags]]
name = "pangloss"
description = "Of or related to the Pangloss individual of interest."

[[tags]]
name = "plague-doctor"
description = "The Plague Doctor, aka SCP-049."

[[tags]]
name = "possessive-mask"
description = "The Possessive Mask, aka SCP-035."

[[tags]]
name = "professor-bjornsen"
description = "Professor Anders Bjornsen."

[[tags]]
name = "rainer-miller"
description = "Rainer Miller, aka SCP-4051."

[[tags]]
name = "researcher-conwell"
description = "Researcher Jacob Conwell."

[[tags]]
name = "researcher-james"
description = "Junior Researcher James, best foundation researcher ever! (Age 5)."

[[tags]]
name = "researcher-labelle"
description = "Researcher Rose Labelle."

[[tags]]
name = "researcher-lloyd"
description = "Researcher Lloyd, Destroyer of Worlds."

[[tags]]
name = "researcher-rosen"
description = "Researcher David Rosen."

[[tags]]
name = "researcher-smalls"
description = "Researcher Adamo Smalls."

[[tags]]
name = "researcher-talloran"
description = "Researcher Talloran."

[[tags]]
name = "richard-chappell"
description = "Richard Davis Chappell, founder of the Chicago Spirit."

[[tags]]
name = "riven-mercer"
description = "Riven Mercer of Kiryu Labs."

[[tags]]
name = "robert-bumaro"
description = "Robert Bumaro, a prophet of Mekhane."

[[tags]]
name = "robin-thorne"
description = "Robin Thorne."

[[tags]]
name = "ruiz-duchamp"
description = "Ruiz Duchamp, an anartist."

[[tags]]
name = "saint-hedwig"
description = "Saint Hedwig, a prophet of Maxwellism."

[[tags]]
name = "saturn-deer"
description = "Saturn Deer."

[[tags]]
name = "scarlet-king"
description = "The Scarlet King."

[[tags]]
name = "sheldon-katz"
description = "Sheldon Katz."

[[tags]]
name = "shy-guy"
description = "The Shy Guy, aka SCP-096."

[[tags]]
name = "sigurros"
description = "Sigurrós Stefánsdóttir, aka SCP-239."

[[tags]]
name = "simon-pietrykau"
description = "Simon Pietrykau."

[[tags]]
name = "tau-5-samsara"
description = "Mobile Task Force Tau-5 'Samsara'."

[[tags]]
name = "thad-xyank"
description = "Dr. Thaddeus \"Thad\" Xyank."

[[tags]]
name = "the-administrator"
description = "The Administrator (as a separate entity from the O5 Council)."

[[tags]]
name = "the-engineer"
description = "The Engineer, of the Chaos Insurgency."

[[tags]]
name = "the-old-man"
description = "The Old Man, aka SCP-106."

[[tags]]
name = "the-sculpture"
description = "The sculpture, aka SCP-173."

[[tags]]
name = "the-specter"
description = "The Specter, aka SCP-4944."

[[tags]]
name = "thilo-zwist"
description = "Thilo Zwist."

[[tags]]
name = "tim-wilson"
description = "Tim Wilson, of Wilson's Wildlife Solutions."

[[tags]]
name = "veronica-fitzroy"
description = "Veronica Katherine Fitzroy, anartist/d-class."

[[tags]]
name = "vincent-anderson"
description = "Vincent Anderson, of Anderson Robotics."

[[tags]]
name = "zyn-kiryu"
description = "Researcher Zyn Kiryu."

[[tags]]
name = "alagadda"
description = "The kingdom of Alagadda."

[[tags]]
name = "backdoor-soho"
description = "The city of Backdoor Soho."

[[tags]]
name = "esterberg"
description = "The Free Port known as Esterberg."

[[tags]]
name = "eurtec"
description = "The metropolis of Eurtec."

[[tags]]
name = "hy-brasil"
description = "The island of Hy-Brasil."

[[tags]]
name = "la-rue-macabre"
description = "The free port of La Rue Macabre."

[[tags]]
name = "three-portlands"
description = "The city of Three Portlands."

[[tags]]
name = "wanderers-library"
description = "The Wanderer's Library."

[[tags]]
name = "adult"
description = "Denotes mature content, view at your own discretion."

[[tags]]
name = "audio"
description = "Used for pages with one or more audio files attached."

[[tags]]
name = "interactive"
description = "The article contains elements that require user input or interaction, e.g. making a decision."

[[tags]]
name = "video"
description = "Used for pages with one or more video files attached."

[[tags]]
name = "in-rewrite"
description = "Used for pages which are currently being rewritten. Utilized by the Rewrite Team."

[[tags]]
name = "rewritable"
description = "Used for pages which are eligible to be rewritten. Utilized by the Rewrite Team."

[[tags]]
name = "rewrite"
description = "This tag indicates that the article in question is a rewrite of another article."

[[tags]]
name = "in-deletion"
description = "Used for pages which which are currently being voted on for deletion."

[[tags]]
name = "featured"
description = "Used for pages which were chosen as features."

[[tags]]
name = "prize-feature"
description = "Used for pages which were chosen as features by the winner of a site contest."

[[tags]]
name = "reviewers-spotlight"
description = "Used for pages which were chosen as features by forum reviewers."

[[tags]]
name = "event-featured"
description = "Used for pages which were chosen as features on special event days."

[[tags]]
name = "metadata"
description = "Used for pages which contain meta information about articles."

[[tags]]
name = "_cc"
description = "Used to indicate that all images on the page are fully compliant with current licensing policy. Utilized by the Licensing Team."

[[tags]]
name = "_image"
description = "Used to indicate that not all images have been verified as being fully compliant with current licensing policy. Utilized by the Licensing Team."

[[tags]]
name = "_licensebox"
description = "Used for pages which have a standard license info block."

[[tags]]
name = "_listpages"
description = "Used for pages which present its article content through offsets served via ListPages."

[[tags]]
name = "_theme-temp"
description = "Used for theme pages which have been migrated from the component category to the theme category."

[[tags]]
name = "crosslink"
description = "Used for pages which is has proposed revisions from the Wikiwalk Subteam of MAST."

[[tags]]
name = "173fest"
description = "An entry to the 173 Festival."

[[tags]]
name = "art-exchange"
description = "Of or related to the Annual Holiday Art Exchange."

[[tags]]
name = "af2014"
description = "Of or related to the Super Cute Pets! 2014 April Fool's prank."

[[tags]]
name = "game-day"
description = "Of or related to the Game Day project."

[[tags]]
name = "nightmarefest"
description = "An entry to the unofficial NIGHTMAREFEST."

[[tags]]
name = "_townhouse"
description = "An entry to the 'Townhouse' category of the unofficial NIGHTMAREFEST."

[[tags]]
name = "_the-bureaucrat"
description = "An entry to the 'The Bureaucrat' category of the unofficial NIGHTMAREFEST."

[[tags]]
name = "_graveyard-shift"
description = "An entry to the 'Graveyard Shift' category of the unofficial NIGHTMAREFEST."

[[tags]]
name = "1000"
description = "An entry to the SCP-1000 Contest."

[[tags]]
name = "2000"
description = "An entry to the SCP-2000 Contest."

[[tags]]
name = "3000"
description = "An entry to the SCP-3000 Contest."

[[tags]]
name = "4000"
description = "An entry to the SCP-4000 Contest."

[[tags]]
name = "5000"
description = "An entry to the SCP-5000 Contest."

[[tags]]
name = "6000"
description = "An entry to the SCP-6000 Contest."

[[tags]]
name = "af2016"
description = "An entry to the Crack Fiction Contest 2016 April Fool's prank."

[[tags]]
name = "art2017"
description = "An entry to the 2017 Art Contest."

[[tags]]
name = "canon2020"
description = "An entry to the 2020 Canon Renaissance Contest."

[[tags]]
name = "cliche2019"
description = "An entry to Cliche-Con 2019."

[[tags]]
name = "collab-con2019"
description = "An entry to Collab-Con 2019."

[[tags]]
name = "cupid2021"
description = "An entry to Cupid Contest 2021."

[[tags]]
name = "d-con2016"
description = "An entry to the 2016 D-Class Contest."

[[tags]]
name = "dc2014"
description = "An entry to the 2014 Dystopia Contest."

[[tags]]
name = "departmentcon2022"
description = "An entry to the 2022 Department Contest."

[[tags]]
name = "doomsday2018"
description = "An entry to the 2018 Doomsday Contest."

[[tags]]
name = "exquisite-corpse2020"
description = "An entry to the 2020 Exquisite Corpse Contest."

[[tags]]
name = "five-questions"
description = "An entry to the Five Questions Contest."

[[tags]]
name = "gbc09"
description = "An entry to 2009 Gears' Birthday Contest."

[[tags]]
name = "goi2014"
description = "An entry to the 2014 Groups of Interest Contest."

[[tags]]
name = "goi2019"
description = "An entry to the International Groups of Interest Contest 2019."

[[tags]]
name = "halloween2018"
description = "An entry to the 2018 Halloween Contest."

[[tags]]
name = "hc2012"
description = "An entry to the 2012 Halloween Contest."

[[tags]]
name = "hiscon2017"
description = "An entry to the 2017 History Contest."

[[tags]]
name = "jam-con2018"
description = "An entry to the 2018 72 Hour Jam Contest."

[[tags]]
name = "_dark-and-stormy"
description = "An entry to the 'Dark and Stormy' category of the 2018 72 Hour Jam Contest."

[[tags]]
name = "_murder-mystery"
description = "An entry to the 'Murder Mystery' category of the 2018 72 Hour Jam Contest."

[[tags]]
name = "_tropical"
description = "An entry to the 'Tropical' category of the 2018 72 Hour Jam Contest."

[[tags]]
name = "jam-con2019"
description = "An entry to the 2019 144-Hour Jam Contest."

[[tags]]
name = "_shaggy-dog"
description = "An entry to the 'Shaggy Dog' category of the 2019 144 Hour Jam Contest."

[[tags]]
name = "_pulp-fiction"
description = "An entry to the 'Pulp Fiction' category of the 2019 144 Hour Jam Contest."

[[tags]]
name = "_all-a-dream"
description = "An entry to the 'All a Dream' category of the 2019 144 Hour Jam Contest."

[[tags]]
name = "jam-con2020"
description = "An entry to the 2020 144-Hour Jam Contest."

[[tags]]
name = "_explosions"
description = "An entry to the 'Explosions' category of the 2020 144 Hour Jam Contest."

[[tags]]
name = "_delicious"
description = "An entry to the 'Delicious' category of the 2020 144 Hour Jam Contest."

[[tags]]
name = "_meets-the-eye"
description = "An entry to the 'Meets the Eye' category of the 2020 144 Hour Jam Contest."

[[tags]]
name = "jam-con2021"
description = "An entry to JamCon 2021."

[[tags]]
name = "_marine"
description = "An entry to the 'Marine' category of JamCon 2021."

[[tags]]
name = "_corruption"
description = "An entry to the 'Corruption' category of JamCon 2021."

[[tags]]
name = "_famouslastwords"
description = "An entry to the '\"What could possibly go wrong?\"' category of JamCon 2021."

[[tags]]
name = "mtf2016"
description = "An entry to the 2016 Mobile Task Force Contest."

[[tags]]
name = "nyc2013"
description = "An entry to the 2013 New Year's Canon Contest."

[[tags]]
name = "rei2015"
description = "An entry to the 2015 Reimagining Contest."

[[tags]]
name = "sc2015"
description = "An entry to the 2015 Short Works Contest."

[[tags]]
name = "tc2013"
description = "An entry to the 2013 Time Contest."

[[tags]]
name = "uac2014"
description = "An entry to the 2014 Under-Appreciated SCPs Contest."

[[tags]]
name = "memecon2021-unofficial"
description = "An entry to the unofficial 2021 MEMECON."

[[tags]]
name = "international"
description = "Applicable if the tale or SCP article was translated from one of the recognized translation sites."

[[tags]]
name = "_int"
description = "Translated from the International Site."

[[tags]]
name = "_ru"
description = "Translated from the Russian Site."

[[tags]]
name = "_ko"
description = "Translated from the Korean Site."

[[tags]]
name = "_cn"
description = "Translated from the Chinese Site."

[[tags]]
name = "_fr"
description = "Translated from the French Site."

[[tags]]
name = "_pl"
description = "Translated from the Polish Site."

[[tags]]
name = "_es"
description = "Translated from the Spanish Site."

[[tags]]
name = "_th"
description = "Translated from the Thai Site."

[[tags]]
name = "_jp"
description = "Translated from the Japanese Site."

[[tags]]
name = "_de"
description = "Translated from the German Site."

[[tags]]
name = "_it"
description = "Translated from the Italian Site."

[[tags]]
name = "_ua"
description = "Translated from the Ukrainian Site."

[[tags]]
name = "_pt"
description = "Translated from the Portuguese Site."

[[tags]]
name = "_zh"
description = "Translated from the Traditional Chinese Site."

[[/code]]
[[/collapsible]]
