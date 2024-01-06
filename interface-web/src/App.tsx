import './App.css'
import { useState } from 'react';
import { useTranslation } from "react-i18next";
import { Image, Text, Stack, HStack, VStack } from "@chakra-ui/react";
import { EmotionsList, EmotionsEmoticon } from './constantsEmotions';

function App() {
  const { t, i18n } = useTranslation();

  const onClickLanguageChange = (e: any) => {
    const language = e.target.value;
    i18n.changeLanguage(language);
  }

  const [language, setLanguage] = useState("fr")

  const onOptionChange = (e: any) => {
    setLanguage(e.target.value)
  }

  const detectedEmotion = 'fear'

  const emoticonEmotion = (emotion: String) => {
    switch (emotion) {
      case EmotionsList[0]:
        return EmotionsEmoticon.ANGER;
      case EmotionsList[1]:
        return EmotionsEmoticon.DISGUST;
      case EmotionsList[2]:
        return EmotionsEmoticon.JOY;
      case EmotionsList[3]:
        return EmotionsEmoticon.NEUTRAL;
      case EmotionsList[4]:
        return EmotionsEmoticon.FEAR;
      case EmotionsList[5]:
        return EmotionsEmoticon.SURPRISE;
      case EmotionsList[6]:
        return EmotionsEmoticon.SADNESS;
    }
  }

  const srcEmotion = emoticonEmotion(detectedEmotion);

  return (
    <Stack className='App'>
      <Stack margin={25}>

        <HStack justifyContent="space-between">
          <Stack></Stack>

          <VStack justifyContent='center' width="95vw">
            <Text marginTop='2vh' marginBottom='10vh' fontSize={35}>
              {t('welcome.title')}
            </Text>
            <VStack bg='#383b40' padding='5vh' borderRadius={30}>
              <Image width={500} height={500} marginBottom='2vh' src={srcEmotion} />
              <Text fontSize={20}>{t('emotion.detected')}</Text>
              <Text fontSize={30}>{t('emotion.list.' + `${detectedEmotion}`)}</Text>
            </VStack>

            <Stack className='Footer' alignSelf='center'>
              <Text fontSize="sm">
                &copy; {new Date().getFullYear()} Created by Marie DOUET, Brice GRINDEL, Lucas MARTIN & Élise SOUVANNAVONG
              </Text>
            </Stack>
          </VStack>

          <VStack width="200px" alignSelf='flex-start'>
            <Text>{t('selection.language')}</Text>
            <HStack onChange={onClickLanguageChange} spacing={25}>
              <VStack><input type="radio" name="language" value="fr" checked={language === "fr"} onChange={onOptionChange} />
                <label><Image width={50} height={35} borderRadius={10} src='https://images.assetsdelivery.com/compings_v2/iconcept123/iconcept1232203/iconcept123220300083.jpg' /></label></VStack>
              <VStack>
                <input type="radio" name="language" value="en" checked={language === "en"} onChange={onOptionChange} />
                <label><Image width={50} height={35} borderRadius={10} src='https://images.assetsdelivery.com/compings_v2/cannonzhooter/cannonzhooter2001/cannonzhooter200100001.jpg' /></label>
              </VStack>
            </HStack>
          </VStack>
        </HStack>



      </Stack >
    </Stack>
  );
}

export default App;
