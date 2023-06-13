import { SearchBar } from "react-native-elements";
import { StyleSheet } from 'react-native';


export default function SearchSteamBar({}) {
    
    return (
        <SearchBar
            placeholder="Search Here..."
            lightTheme
            round
            value={''}
            onChangeText={''}
            autoCorrect={false}
        />
    );
    
};
  