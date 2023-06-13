import { StyleSheet, Text, View } from 'react-native';
import SearchSteamBar from './components/SearchSteamBar'

export default function App() {

  return (
    <View style={styles.container}>
      <SearchSteamBar/>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    display: 'flex',
    flexDirection: 'column',
    justifyContent: 'flex-start',
    alignItems: 'stretch',
    alignContent: 'center',
    backgroundColor: '#fff',
  },
});
