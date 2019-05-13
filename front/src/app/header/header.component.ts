import { Component, OnInit } from '@angular/core';
import { Item } from './item';
@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent implements OnInit {
  public items: Item[] = [
    { title: 'Home', link: '#' },
    { title: 'Orders', link: '/product' },
    { title: 'Profile', link: '#' },
]

  constructor() { }

  ngOnInit() {
  }

}