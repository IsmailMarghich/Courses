import { User } from "./User"; /*import our user and company class*/
import { Company } from "./Company";
import { CustomMap } from "./CustomMap";

const user = new User();
const company = new Company();
const customMap = new CustomMap("map");

customMap.addMarker(user);
customMap.addMarker(company);
