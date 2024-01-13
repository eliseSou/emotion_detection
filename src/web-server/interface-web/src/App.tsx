import './App.css'
import { useState } from 'react';
import { useTranslation } from "react-i18next";
import { Image, Text, Stack, HStack, VStack } from "@chakra-ui/react";
import CardEmotion from './Components/CardEmotion';

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

  return (
    <Stack className='App'>
      <Stack margin={25}>

        <HStack justifyContent="space-between">
          <Stack></Stack>

          <VStack justifyContent='center' width="95vw">
            <Stack marginTop='2vh' marginBottom='10vh' fontSize={35} alignItems='center' > 
              <Text>
                {t('welcome.titleBefore')}
              </Text>
              <HStack>
                <Text bgGradient='linear(to-r, #FFB286, #FF0080)' bgClip='text' fontWeight='extrabold'>
                  Emoticall
                </Text>
                <Text>
                  {t('welcome.titleAfter')}
                </Text>
              </HStack>
            </Stack>

            <CardEmotion/>

            <Stack className='Footer' alignSelf='center'>
              <Text fontSize="sm">
                &copy; {new Date().getFullYear()} {t('welcome.footer')}
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
