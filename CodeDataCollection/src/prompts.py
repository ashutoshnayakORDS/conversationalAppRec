
class PromptsDataCollection():
    def __init__(self, name, description):
        self.name         = name
        self.description  = description
        self.geminiPrompt = f"""You are given an app store optimization specialist, with an expertise in optimizing app metadata, including descriptions, to improve app visibility and downloads.
                                You are given the following name and the description of the app below.

                                ------------------------
                                Name of the app: {self.name}
                                Description of the app: {self.description}

                                based on the description of the app, follow the step-by-step guide below:
                                1-summarize what the mobile app is about within 250 words. sumamry should be informative and DO NOT ANY EXTERNAL INFORMATION
                                2-decription may have features inforamtion. identify these main features of the app. ONLY if featuers are not givem, identify from the summary you created.
                                3-find adjectives for the app which should attract users
                                4-find 4-5 search keywords as who is the target audience for whom is the app designed for.

                                Output in the following text format. Strictly follow the format. NO special characters.

                                summary: summary of the app withinn 250 words
                                features: main features of the app
                                adjectives:best 4-5 adjectives for the app
                                search_term:keywords of 4-5 target audience for whom is the app designed for/words that would atttract users to this app
                            """