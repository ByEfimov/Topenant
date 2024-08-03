import type { IUser } from './user';
import type { IWork } from './works';

export interface ICompany {
    id: number;
    name: string;
    rating: number;
    image: string;
    applicant: boolean;
    pointsHave: number;
    employer: IUser;
    works: IWork[];
}
