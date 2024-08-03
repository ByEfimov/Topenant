import type { ICompany } from './company';
import type { IUser } from './user';

export interface IWork {
    id: number;
    company: ICompany;
    title: string;
    description: string;
    image: string;
    rating: number;
    pointsToGive: number;
    timeToJob: number;
}

export type TTicketStatuses = 'rejected' | 'approved' | 'waiting';

export interface ISendTicket {
    status: TTicketStatuses;
    work: number;
    applicant: number;
}
export interface ITicket {
    id: number;
    status: TTicketStatuses;
    work: IWork;
    applicant: IUser;
}
