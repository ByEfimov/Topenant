export type TUserRoles = 'employer' | 'applicant';

export interface IUser {
    id: number;
    name: string;
    email: string;
    phone: string;
    role: TUserRoles;
    points: number;
}

export interface IUserForm extends IUser {
    password: string;
}
