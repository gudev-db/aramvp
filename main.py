import streamlit as st
import google.generativeai as genai
from tavily import TavilyClient
import requests
import os

# Configuração das APIs
gemini_api_key = os.getenv("GEM_API_KEY")
t_api_key1 = os.getenv("T_API_KEY")
rapid_key = os.getenv("RAPID_API")

# Configura o cliente Gemini
genai.configure(api_key=gemini_api_key)
modelo_linguagem = genai.GenerativeModel("gemini-1.5-flash")

report_model = '''
SCO Summit in Astana: Russia's Strategy
In early July 2024, Astana will host the Shanghai Cooperation Organization (SCO)summit, where around 30 documents are expected to be reviewed and thedecision on Belarus' membership in the organization will be signed. The theme ofthe meeting is "Strengthening Multilateral Dialogue — Pursuing Sustainable Peaceand Development."

Key Considerations of Russia and its Leadership Participating in theSCO Summit
Regional Security and Threat Mitigation
Facing numerous threats on its southern borders, Russia views the SCO as animportant platform for security cooperation. The organization serves as amechanism for coordinating efforts in combating terrorism, extremism, and drugtrafficking, which is crucial for stability in Central Asia and Russia's border regions.Amid rising geopolitical tensions, the Russian leadership is preparing proposals toenhance the security component within the SCO framework. Russia believes it isnecessary to have close interaction among the institutions of SCO membercountries responsible for security.

Russia also believes that SCO members share a common desire to coordinate theorganization's actions at the UN and in the Eurasian space with structures like theEAEU, ASEAN, and BRICS. Since its establishment in 2001, the SCO has grownfrom a regional bloc ensuring security around the post-Soviet states and Chinainto a structure aspiring to be a guarantor of comprehensive Eurasian security.
The organization now includes countries like Iran, India, and Pakistan, with Belarussoon to join.


Enhanced Cooperation on Security Issues
In recent years, the SCO has intensified its cooperation on regional security issues.
In 2023, Kazakhstan participated in the first joint anti-terrorism exercises of theSCO and CIS, "Eurasia-Antiterror," and in joint exercises with Uzbekistan, "Kanzhar-2023," aimed at combating an international terrorist organization. At the end of2023, the "Combat Fellowship" exercises were held with the participation ofmilitary personnel from CIS countries.
The crisis in international security architecture is driving regional integration. Thegrowing interest of non-Western players in the SCO reflects current internationaltrends of declining trust in North Atlantic institutions. By joining the SCO,countries of the Global South demonstrate their independence and prioritize thisplatform for security.


Russia's Proposals for Strengthening Cooperation
In light of this, Russia is preparing proposals for SCO member countries toenhance cooperation not only in ensuring the security of the organization's
common space but also in strengthening military-technical cooperation. Russiaaims to use the summit to promote military-technical cooperation, including thesupply of weapons and the conduct of joint military exercises. This will helpbolster the defense capabilities of SCO member countries and enhance theirability to counter common threats. This aspect is particularly important for Russia,which is in global confrontation with the West and engaged in conflict in Ukraine.By advancing cooperation on military-technical lines, Russia seeks to compensatefor the technological shortfall faced by its military-industrial complex in producingweapons for the war in Ukraine.
This is especially critical against the backdrop of the US decision to supplyUkraine with advanced weapons, including F-16 fighter jets. For the production ofnew Su-30 and Su-35 fighters, as well as the completion of S-400 air defensesystems, Russia needs new technological components such as chips andmicrocircuits.
To address the problem of technological dependence on the West, Russia isactively considering the idea of creating a common technological market withinthe SCO. The goal of this initiative is to foster cooperation in high technology andinnovation by establishing joint institutes for developing new technologies andfinancing mechanisms, as well as mechanisms for active and rapid technologicalexchange and transfer among the member countries of the organization.


Economic Cooperation and Development
In the face of Western sanctions, Russia is actively seeking opportunities todiversify its economic ties. The SCO summit provides an excellent platform forsigning new trade agreements, attracting investments, and developing jointprojects in sectors such as energy, transport, and infrastructure. Russia is alsointerested in expanding its exports of goods and services to SCO member markets.
This could involve agreements on energy supplies, the development of transportcorridors, and joint industrial projects. Particularly important could be cooperationin high technologies and innovations.


Strategic Pivot to the East
In its global strategy to pivot to the East, it is crucial for Russia to increase thesupply of its energy resources to SCO countries' markets. Amid disagreementswith China over gas prices related to the still unrealized "Power of Siberia - 2"project, Russia intends to make a strategic move by presenting two proposalsaimed at exerting pressure on Beijing. First, the Russian leadership is consideringimposing a recycling fee on imported cars, which would increase the cost of carsimported from China, thereby reducing their competitiveness in the Russianmarket.
This decision by the Russian leadership also has a "domestic social base" in theform of supporting local car manufacturers. In March, the head of AvtoVAZ,Maxim Sokolov, spoke about the "aggressive expansion" of Chinese car companiesinto the Russian market, saying they are entering traditional Lada market
segments by offering large discounts that offset the recycling fee.
The process has already begun. On June 13, Duma deputies submitted a draft lawto the government that provides for an increase in the recycling fee. Theindexation is planned until 2030, and the amount could increase fourfold by theend of the period.


Impact on Car Prices and Local Manufacturers
The Russian Ministry of Economic Development has already supported the latestincrease in the recycling fee. If the draft law is passed, the fee for passenger carswith engine capacities between 1 and 2 liters will increase from 300,000 rubles to550,000 rubles this year, to 660,000 rubles in 2025, and almost to 1 million rublesby 2029. By 2030, the recycling fee could increase fourfold. Consequently, if thelaw is passed, car prices could rise by an average of 300,000 rubles in the nearfuture.
The gradual increase in the recycling fee is designed to protect domesticmanufacturers. The Russian government's initiative to raise duties on the importof passenger cars with engine capacities between 1 and 2 liters by four times isaimed at strengthening the positions of Russian manufacturers, as the demand fordomestic cars is not growing.


Strengthening Energy Cooperation with India
Another initiative of the Russian government, currently in the development stage,is to enhance energy cooperation with India, a regional competitor to China.
Moscow and Delhi are already actively cooperating in the energy sector, withRussia significantly increasing its energy exports to India since 2022. Now, amidthe dispute with China over gas prices, Moscow intends to offer discounts forother markets for Russian gas and oil supplies, particularly to India, which hasbeen earning from exporting petroleum products to Europe produced fromRussian crude for several years.


LNG Infrastructure and Long-Term Prospects
The infrastructure for supplying Russian gas to India is not direct but is carried outthrough swap mechanisms. Currently, gas is supplied from Cameroon to Indiaunder a swap scheme within the Gazprom Marketing & Trading portfolio (whichwas renamed SEFE after being seized by Germany), while gas from "Yamal LNG" isdirected to other recipients. Plans are in place to activate this mechanism further.
Large-scale LNG production in Russia is carried out by "Sakhalin Energy" (ownedby Gazprom, Mitsui, and Mitsubishi) and "Yamal LNG" (owned by NOVATEK,TotalEnergies, and Chinese CNPC and SRF). In the long term, expectations of theglobal LNG market's growth are linked with India, China, and Southeast Asiancountries.


What Goals Might Russia Be Pursuing Through the SCO and the
Upcoming Summit?
Russia aims to strengthen its political influence in the region and on the globalstage by using the Shanghai Cooperation Organization (SCO) as a tool todemonstrate leadership. Participation in the organization allows Russia toenhance ties with China, India, and other key players, which helps shape amultipolar world and reduce Western dominance in global politics.
The SCO is a crucial element of Russia's strategy to promote the idea of amultipolar world. Russia views the organization as a platform for uniting theefforts of countries seeking a fair and balanced international order. This isespecially important in the context of current geopolitical tensions and the desireto reduce dependence on Western institutions.
Signing New Economic Agreements
Russia may aim to sign new trade and investment agreements with SCO members.
These could include arrangements for the supply of energy resources, thedevelopment of transport corridors, and joint industrial projects. Cooperation inhigh technologies and innovations could become a particularly importantdirection.

Promoting Infrastructure Initiatives
One of Russia's key goals is to promote large infrastructure projects, such as thecreation of transport corridors linking Europe and Asia. These projects cancontribute to the economic development of the region and strengthen trade tiesbetween SCO member countries.

Supporting Stability in Central Asia
Russia is interested in maintaining stability in Central Asia, which is important forits own security. The summit provides an opportunity to discuss measures forconflict prevention and regional stabilization, as well as joint actions to respond tocrisis situations.


Moscow's Assessment of the Opportunities and Challenges Facing theDevelopment of the SCO
In its early days, the Shanghai Cooperation Organization (SCO) primarilyfunctioned to protect member states from the growing terrorist threat emanatingfrom Afghanistan. Today, while the Afghan issue remains significant, it is nolonger the sole focus of the organization. The expansion of countries involved inSCO activities indicates that the platform is seriously vying for the status of analternative to the North Atlantic project as a guarantor of comprehensive Eurasiansecurity.
Among the key areas of SCO activity is the Afghan issue, which remains one of themost critical for regional stability. In 2023, the SCO countries issued a declaration
at the New Delhi summit, advocating for Afghanistan to become an independent,united, and neutral state. However, in practice, it is still premature to speak ofresolving the Afghan problem solely through SCO efforts. This is primarily due todiffering approaches among member states regarding how to engage with theTaliban-led Afghanistan. The Taliban's rise to power in 2021 has complicated thealready challenging process of consolidation within the SCO. To date, there hasbeen little progress on forming an inclusive Afghan government, despite the SCOmembers' calls for a government representing all ethnic groups in the country.
Russia, in general, supports Afghanistan's accession to the SCO and is preparingto remove the Taliban from its list of terrorist organizations. On May 27, theRussian Ministry of Foreign Affairs and the Ministry of Justice recommended thatPresident Vladimir Putin exclude the Taliban from the list of banned organizations.
President Putin has already stated that, since the Taliban currently control all ofAfghanistan, "Moscow will build relations with their representatives based ontoday's realities." On June 3, Kazakhstan removed the Taliban from its list ofterrorist organizations.
Russia is also actively developing trade and economic ties with Afghanistan underits new leadership. According to the Afghan Chamber of Commerce andInvestment, bilateral trade turnover could reach $600 million this year, up fromjust $170 million in 2022. Afghanistan primarily imports petroleum products, food,medicines, and other consumer goods from Russia. As the security situationimproves, Russian private businesses are increasingly signing contracts withAfghan partners.
There are also plans for cooperation between Moscow and Afghanistan within theframework of the Collective Security Treaty Organization (CSTO). While suchcooperation has not yet occurred, it is considered likely, especially sinceAfghanistan borders the CSTO's area of responsibility in Central Asia.
After President Putin positively considers removing the Taliban from the list ofbanned organizations in Russia, Moscow will seek the lifting of internationalsanctions on certain Taliban leaders in the UN Security Council.
Afghanistan's inclusion in the SCO would enhance the country's trade andeconomic interactions not only with Russia but also with all regional states.
Moreover, it would help to lift Afghanistan out of international isolation and assistthe new government in stabilizing the country's economic situation. Continuedisolation would likely increase the influence of transnational extremistorganizations both within Afghanistan and beyond its borders. Therefore,neighboring countries must engage with the Taliban.
Although Tajikistan maintains a hostile stance towards the new Afghan authorities,Moscow could overcome Dushanbe's resistance to Kabul's SCO membership,especially following the terrorist attack in the Moscow suburb of Crocus City,carried out by the Central Asian branch of ISIS.


The Growing Heterogeneity of the SCO
As the list of SCO member countries expands, the organization is becomingincreasingly heterogeneous, leading to rising contradictions among its members.
Notable examples include the Indo-Pakistani territorial issue, border disputesbetween Tajikistan and Kyrgyzstan, and tensions surrounding Iran. FollowingBelarus's accession to the SCO, the organization will have a member for whomregional terrorism and extremism are relevant but not as pressing as they are forregional players.
Additionally, there is a notable difference in the perceived importance of the SCObetween Russia and China. For Russia, the SCO's potential in ensuring Eurasiansecurity is significantly linked to anti-Western discourse and aligning positionswith China, India, and possibly Iran. Although the SCO has not offered aconsolidated stance on Russia's special operation in Ukraine, its rhetoric stilldistances itself from the Western-centric model. The SCO offers alternatives notonly in security but also in economic development, such as reducing the use of thedollar in mutual settlements, increasing trade turnover, and converging financialand banking institutions. However, a unified position on an anti-sanctionsstrategy has not been developed among member states, despite growing tradebetween Russia and SCO countries.
For China, the SCO primarily serves as a security guarantee for the ambitious Beltand Road Initiative, providing strategic support for infrastructure and logisticsprojects along its route. While the SCO is significant for China as an alternativepower center to the US in Asia (especially given the American anti-China initiativeAUKUS in the Asia-Pacific region), this aspect has not become central for Chineseleadership. Like Russia, China addresses security issues within the SCO mainlythrough bilateral interactions. China views consensus in Eurasia as thedevelopment of a unified development strategy, economically supported.
Sources
Sources A, Assistant to the President.
Sources B, Chairman of the Foreign Affairs.
Sources C, Head of the Council on Foreign and Defense Policy of XXX[country].



'''

def osint_report():
    st.subheader("Intelligence report generator")

    # Input do usuário
    intelligence = st.text_area("Write here the information for your report:")
    
    # Botão para gerar o relatório
    if st.button("Generate intelligence report"):
        if intelligence.strip():  # Verifica se o input não está vazio
            with st.spinner("Generating..."):
                prompt = f"""
                    -You are a well read, educated, highly skilled intelligence report writer. The user has made scribbles after interviewing a person
                    of interest. your goal is to write an intelligence report from those scribbles.
                    
                    
                    
                    -Based on the writing and format of the previous report, write a new one with these key informations:
                    {intelligence}
                """
                
                # Gera o relatório com Gemini
                response = modelo_linguagem.generate_content(prompt)
                osint_report_output = response.text if response else "Erro ao gerar o relatório."
                
                # Exibe o relatório no Streamlit
                st.subheader("Relatório de Inteligência Gerado")
                st.markdown(osint_report_output)
        else:
            st.warning("Por favor, preencha o campo para gerar o relatório.")

# Executa a função principal
osint_report()
