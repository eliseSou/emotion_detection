import './App.css'
import { useState } from 'react';
import { useTranslation } from "react-i18next";
import { Image, Text, Stack, useToast, HStack, VStack } from "@chakra-ui/react";
import { EmotionsList, Emotions } from './constantsEmotions';

function App() {
  const { t, i18n } = useTranslation();
  const toast = useToast();

  const onClickLanguageChange = (e: any) => {
    const language = e.target.value;
    i18n.changeLanguage(language);
  }

  const [language, setLanguage] = useState("fr")

  const onOptionChange = (e: any) => {
    setLanguage(e.target.value)
  }

  const changeEmotion = (emotion: String) => {
    switch (emotion) {
      case EmotionsList[0]:
        return Emotions.ANGER;
      case EmotionsList[1]:
        return Emotions.DISGUST;
      case EmotionsList[2]:
        return Emotions.JOY;
      case EmotionsList[3]:
        return Emotions.NEUTRAL;
      case EmotionsList[4]:
        return Emotions.FEAR;
      case EmotionsList[5]:
        return Emotions.SURPRISE;
      case EmotionsList[6]:
        return Emotions.SADNESS;
    }
  }

  const srcEmotion = changeEmotion('joy');

  return (
    <Stack className="App" height="100vh" bg="#2b2d31" textColor="white">
      <Stack margin={25}>

        <HStack justifyContent="space-between">
          <Stack></Stack>

          <VStack justifyContent='center'>
            <Text width="80vw" fontSize={30}>
              {t('welcome.title')}
            </Text>
            <Image width={500} height={500} borderRadius={10} marginTop='10vh' src={srcEmotion} />
          </VStack>

          <VStack width="15vw" alignSelf='flex-start'>
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
