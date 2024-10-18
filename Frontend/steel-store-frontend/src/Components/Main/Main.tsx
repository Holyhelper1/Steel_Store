import { SearchBar } from "../Header/Search_bar/Search_bar";
import { ChooserHeader } from "../Product-Chooser/Chooser-header/Chooser-header";
import { ChooserInfo } from "../Product-Chooser/Chooser-info/Chooser-info";

export const Main = () => {
    return (
        <div>
            <SearchBar />
            <ChooserHeader />
            <ChooserInfo />
        </div>
    );
};